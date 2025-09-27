#!/usr/bin/env python3
"""Utilities for validating and packaging the production EPUB and PDF outputs.

This tool centralises the quality checks that were previously spread across
individual scripts.  It performs three major tasks:

1. **Validation** – confirm XHTML structure, asset references, CSS links and
   accessibility-related requirements (such as image alt text) prior to
   packaging.
2. **EPUB assembly** – compile the validated source into a distributable
   `.epub` file with the correct container structure.
3. **PDF generation** – build a print-ready PDF that mirrors the EPUB reading
   order using `wkhtmltopdf` (or another command supplied by the user).

The script intentionally operates on the `output/OEBPS` directory so that we do
not accidentally alter the in-progress source found in `input/`.  All generated
artifacts are written into the `dist/` directory to match the existing project
conventions.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import xml.etree.ElementTree as ET


XHTML_NS = "http://www.w3.org/1999/xhtml"
OPF_NS = "http://www.idpf.org/2007/opf"


def _normalise_css_url(value: str) -> Optional[str]:
    """Normalise the value extracted from a CSS ``url()`` declaration."""

    value = value.strip().strip("'\"")
    if not value or value.startswith("data:") or "://" in value:
        return None
    return value


@dataclass
class ValidationReport:
    """Aggregate information about discovered validation issues."""

    missing_assets: List[Tuple[Path, str, Path]] = field(default_factory=list)
    missing_alt_text: List[Tuple[Path, str]] = field(default_factory=list)
    unresolved_css_assets: List[Tuple[Path, str]] = field(default_factory=list)

    def is_clean(self) -> bool:
        return not (self.missing_assets or self.missing_alt_text or self.unresolved_css_assets)

    def summarise(self) -> None:
        if not self.missing_assets:
            print("  ✓ All referenced assets resolved")
        else:
            print(f"  ✗ Missing assets ({len(self.missing_assets)}):")
            for xhtml, reference, target in self.missing_assets:
                print(f"    - {xhtml.relative_to(Path.cwd())}: '{reference}' → {target}")

        if not self.missing_alt_text:
            print("  ✓ All <img> tags provide alt text")
        else:
            print(f"  ✗ Images without alt text ({len(self.missing_alt_text)}):")
            for xhtml, img_id in self.missing_alt_text:
                location = img_id or "<img>"
                print(f"    - {xhtml.relative_to(Path.cwd())} → {location}")

        if not self.unresolved_css_assets:
            print("  ✓ All CSS url() references resolved")
        else:
            print(f"  ✗ Missing CSS assets ({len(self.unresolved_css_assets)}):")
            for css_file, reference in self.unresolved_css_assets:
                print(f"    - {css_file.relative_to(Path.cwd())}: '{reference}'")


@dataclass
class ProductionBuilder:
    project_root: Path = field(default_factory=lambda: Path.cwd())
    source_root: Path = field(default_factory=lambda: Path.cwd() / "output")
    meta_root: Path = field(default_factory=lambda: Path.cwd() / "META-INF")
    mimetype_path: Path = field(default_factory=lambda: Path.cwd() / "mimetype")
    package_path: Path = field(default_factory=lambda: Path.cwd() / "package.opf")
    dist_dir: Path = field(default_factory=lambda: Path.cwd() / "dist")
    epub_name: str = "unveiling-your-creative-odyssey.epub"
    pdf_name: str = "unveiling-your-creative-odyssey.pdf"

    def __post_init__(self) -> None:
        self.project_root = self.project_root.resolve()
        self.source_root = self.source_root.resolve()
        self.meta_root = self.meta_root.resolve()
        self.mimetype_path = self.mimetype_path.resolve()
        self.package_path = self.package_path.resolve()
        self.dist_dir = self.dist_dir.resolve()

        self.xhtml_dir = self.source_root / "OEBPS" / "text"
        self.styles_dir = self.source_root / "OEBPS" / "styles"

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------
    def _ensure_structure(self) -> None:
        required_paths = [
            (self.source_root / "OEBPS").resolve(),
            self.xhtml_dir,
            self.styles_dir,
        ]

        print("🔍 Checking directory structure...")
        for path in required_paths:
            if not path.exists():
                raise FileNotFoundError(f"Required path missing: {path}")
            print(f"  • {path.relative_to(self.project_root)}")

    def _resolve_asset(self, xhtml_file: Path, reference: str) -> Optional[Path]:
        candidate = (xhtml_file.parent / reference).resolve()
        try:
            candidate.relative_to(self.source_root)
        except ValueError:
            return None
        return candidate if candidate.exists() else None

    def validate(self) -> ValidationReport:
        self._ensure_structure()

        report = ValidationReport()
        ET.register_namespace("x", XHTML_NS)

        print("🧾 Validating XHTML assets...")
        for xhtml_file in sorted(self.xhtml_dir.glob("*.xhtml")):
            try:
                tree = ET.parse(xhtml_file)
            except ET.ParseError as exc:
                raise RuntimeError(f"Failed to parse {xhtml_file}: {exc}") from exc

            root = tree.getroot()
            namespace = {"x": XHTML_NS}

            # Validate linked stylesheets and images
            for link in root.findall('.//x:link[@rel="stylesheet"]', namespace):
                href = link.attrib.get("href", "").strip()
                if not href:
                    continue
                target = self._resolve_asset(xhtml_file, href)
                if target is None:
                    report.missing_assets.append((xhtml_file, href, (xhtml_file.parent / href).resolve()))

            for image in root.findall('.//x:img', namespace):
                src = image.attrib.get("src", "").strip()
                if src:
                    target = self._resolve_asset(xhtml_file, src)
                    if target is None:
                        report.missing_assets.append((xhtml_file, src, (xhtml_file.parent / src).resolve()))
                else:
                    report.missing_assets.append((xhtml_file, "<empty src>", xhtml_file))

                alt_text = image.attrib.get("alt")
                if alt_text is None or not alt_text.strip():
                    image_id = image.attrib.get("id", "")
                    report.missing_alt_text.append((xhtml_file, image_id))

        print("🎨 Validating CSS asset references...")
        url_pattern = re.compile(r"url\(([^)]+)\)")
        css_dir = self.styles_dir
        if css_dir.exists():
            for css_file in sorted(css_dir.glob("*.css")):
                content = css_file.read_text(encoding="utf-8")
                for match in url_pattern.findall(content):
                    ref = _normalise_css_url(match)
                    if not ref:
                        continue
                    target = (css_file.parent / ref).resolve()
                    try:
                        target.relative_to(self.source_root)
                    except ValueError:
                        report.unresolved_css_assets.append((css_file, ref))
                        continue
                    if not target.exists():
                        report.unresolved_css_assets.append((css_file, ref))

        print("📋 Validation summary:")
        report.summarise()
        return report

    # ------------------------------------------------------------------
    # EPUB assembly
    # ------------------------------------------------------------------
    def build_epub(self, *, force: bool = False) -> Path:
        report = self.validate()
        if not report.is_clean() and not force:
            raise SystemExit("Validation issues detected. Re-run with --force to continue anyway.")

        if not self.mimetype_path.exists():
            raise FileNotFoundError(f"mimetype file not found at {self.mimetype_path}")
        if not self.meta_root.exists():
            raise FileNotFoundError(f"META-INF directory not found at {self.meta_root}")

        self.dist_dir.mkdir(parents=True, exist_ok=True)
        epub_path = self.dist_dir / self.epub_name

        print("📦 Building EPUB package...")
        with tempfile.TemporaryDirectory() as tmp_dir:
            staging = Path(tmp_dir)
            shutil.copytree(self.source_root / "OEBPS", staging / "OEBPS", dirs_exist_ok=True)
            shutil.copytree(self.meta_root, staging / "META-INF", dirs_exist_ok=True)

            with zipfile.ZipFile(epub_path, "w") as epub_zip:
                epub_zip.write(self.mimetype_path, "mimetype", compress_type=zipfile.ZIP_STORED)
                for root_dir, _dirs, files in os.walk(staging):
                    for filename in files:
                        file_path = Path(root_dir) / filename
                        rel_path = file_path.relative_to(staging)
                        epub_zip.write(file_path, str(rel_path))

        print(f"✅ EPUB written to {epub_path}")
        return epub_path

    # ------------------------------------------------------------------
    # PDF generation
    # ------------------------------------------------------------------
    def _spine_order(self) -> List[Path]:
        if not self.package_path.exists():
            return sorted(self.xhtml_dir.glob("*.xhtml"))

        tree = ET.parse(self.package_path)
        ns = {"opf": OPF_NS}

        manifest: Dict[str, str] = {}
        for item in tree.findall(".//opf:manifest/opf:item", ns):
            item_id = item.attrib.get("id")
            href = item.attrib.get("href")
            if item_id and href and href.endswith(".xhtml"):
                manifest[item_id] = href

        order: List[Path] = []
        for itemref in tree.findall(".//opf:spine/opf:itemref", ns):
            idref = itemref.attrib.get("idref")
            if not idref:
                continue
            href = manifest.get(idref)
            if not href:
                continue
            order.append((self.source_root / "OEBPS" / href).resolve())

        # Fallback if the manifest/spine did not produce any results.
        if not order:
            order = sorted(self.xhtml_dir.glob("*.xhtml"))

        return [path for path in order if path.exists()]

    def build_pdf(self, *, command: Sequence[str] | None = None, page_size: str = "Letter") -> Path:
        pdf_command = list(command) if command else None

        if pdf_command is None:
            wkhtmltopdf = shutil.which("wkhtmltopdf")
            if not wkhtmltopdf:
                raise SystemExit(
                    "wkhtmltopdf is not available. Install it or pass a custom command via --pdf-command."
                )
            pdf_command = [
                wkhtmltopdf,
                "--quiet",
                "--enable-local-file-access",
                "--page-size",
                page_size,
                "--margin-top",
                "20mm",
                "--margin-bottom",
                "20mm",
                "--margin-left",
                "20mm",
                "--margin-right",
                "20mm",
            ]

        xhtml_files = self._spine_order()
        if not xhtml_files:
            raise SystemExit("No XHTML files found for PDF generation")

        print("🖨️ Generating print-ready PDF...")
        input_urls = [f"file://{path}" for path in xhtml_files]
        self.dist_dir.mkdir(parents=True, exist_ok=True)
        pdf_path = self.dist_dir / self.pdf_name

        command_line = pdf_command + input_urls + [str(pdf_path)]
        result = subprocess.run(command_line, capture_output=True, text=True)
        if result.returncode != 0:
            sys.stderr.write(result.stderr)
            raise SystemExit(f"PDF generation failed with exit code {result.returncode}")

        print(f"✅ PDF written to {pdf_path}")
        return pdf_path


def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate and package the EPUB/PDF deliverables.")
    parser.add_argument("command", choices=["validate", "epub", "pdf", "all"], help="Action to perform")
    parser.add_argument("--force", action="store_true", help="Build even if validation warnings are present")
    parser.add_argument(
        "--pdf-command",
        nargs=argparse.REMAINDER,
        help="Override the PDF command. Everything after this flag is treated as the command.",
    )
    parser.add_argument("--page-size", default="Letter", help="Page size for PDF output (default: Letter)")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = parse_arguments(argv)
    builder = ProductionBuilder()

    if args.command == "validate":
        report = builder.validate()
        if not report.is_clean():
            raise SystemExit(1)
        return

    if args.command == "epub":
        builder.build_epub(force=args.force)
        return

    if args.command == "pdf":
        builder.build_pdf(command=args.pdf_command, page_size=args.page_size)
        return

    if args.command == "all":
        builder.build_epub(force=args.force)
        builder.build_pdf(command=args.pdf_command, page_size=args.page_size)
        return


if __name__ == "__main__":
    main()
