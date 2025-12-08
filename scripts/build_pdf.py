#!/usr/bin/env python3
"""
Print-on-Demand PDF Compilation Script

Compiles all XHTML chapters into a single professional POD-ready PDF.
Uses headless Chrome/Playwright for accurate CSS rendering.

Usage:
    python3 scripts/build_pdf.py --source REBRANDED_OUTPUT --output dist/book.pdf
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional

try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("WARNING: playwright not installed. Install with: pip install playwright && playwright install chromium")


class PDFCompiler:
    """Compile XHTML chapters into single POD PDF."""

    def __init__(self, source_dir: Path, output_path: Path, targets_json: Optional[Path] = None):
        self.source_dir = source_dir.resolve()
        self.output_path = output_path.resolve()
        self.targets_json = targets_json
        self.chapters = []

    def load_chapters(self) -> bool:
        """Load chapter list from content.opf spine."""

        if self.targets_json and self.targets_json.exists():
            # Use existing targets JSON
            print(f"Loading chapters from: {self.targets_json}")
            with open(self.targets_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.chapters = [item['xhtml_path'] for item in data.get('targets', [])]
        else:
            # Parse content.opf
            print("Parsing content.opf for chapter order...")
            opf_path = self.source_dir / "content.opf"
            if not opf_path.exists():
                print(f"ERROR: content.opf not found at {opf_path}")
                return False

            # Simple XML parsing to extract spine order
            import xml.etree.ElementTree as ET
            tree = ET.parse(opf_path)
            root = tree.getroot()

            # Define namespace
            ns = {'opf': 'http://www.idpf.org/2007/opf'}

            # Get manifest items
            manifest = {}
            for item in root.findall('.//opf:manifest/opf:item', ns):
                item_id = item.get('id')
                href = item.get('href')
                if href and href.endswith('.xhtml'):
                    manifest[item_id] = href

            # Get spine order
            for itemref in root.findall('.//opf:spine/opf:itemref', ns):
                idref = itemref.get('idref')
                if idref in manifest:
                    self.chapters.append(manifest[idref])

        print(f"  ✓ Found {len(self.chapters)} chapters")
        return len(self.chapters) > 0

    def compile_pdf(self) -> bool:
        """Compile all chapters into single PDF using Playwright."""

        if not PLAYWRIGHT_AVAILABLE:
            print("ERROR: Playwright is required for PDF compilation")
            print("Install: pip install playwright && playwright install chromium")
            return False

        print(f"\n[1/3] Loading chapters...")
        if not self.load_chapters():
            return False

        print(f"\n[2/3] Rendering {len(self.chapters)} chapters to PDF...")
        print("This may take several minutes...")

        # Create output directory
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            # Collect all rendered pages
            temp_pdfs = []

            for idx, chapter_path in enumerate(self.chapters, 1):
                full_path = self.source_dir / chapter_path
                if not full_path.exists():
                    print(f"  ⚠ Skipping missing file: {chapter_path}")
                    continue

                # Navigate to XHTML file
                file_url = f"file://{full_path}"
                page.goto(file_url, wait_until="networkidle")

                # Wait for fonts and images to load
                page.wait_for_timeout(500)

                # Generate individual PDF
                temp_pdf = self.output_path.parent / f"temp_chapter_{idx:03d}.pdf"
                page.pdf(
                    path=str(temp_pdf),
                    format="Letter",  # 8.5" x 11" for POD
                    print_background=True,
                    margin={
                        "top": "0.75in",
                        "right": "0.75in",
                        "bottom": "0.75in",
                        "left": "0.75in"
                    }
                )
                temp_pdfs.append(temp_pdf)

                if idx % 5 == 0:
                    print(f"    Rendered {idx}/{len(self.chapters)} chapters...")

            browser.close()

        print(f"  ✓ Rendered {len(temp_pdfs)} chapters")

        # Merge PDFs using PyPDF2 or reportlab
        print(f"\n[3/3] Merging PDFs into final document...")
        merge_success = self._merge_pdfs(temp_pdfs)

        # Cleanup temp files
        for temp_pdf in temp_pdfs:
            temp_pdf.unlink()

        if not merge_success:
            print("ERROR: PDF merge failed")
            return False

        # Report
        file_size = self.output_path.stat().st_size
        file_size_mb = file_size / (1024 * 1024)

        print("\n" + "=" * 60)
        print("PDF BUILD COMPLETE")
        print("=" * 60)
        print(f"Output file: {self.output_path}")
        print(f"File size: {file_size_mb:.2f} MB")
        print(f"Chapters: {len(temp_pdfs)}")
        print(f"Build time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)

        return True

    def _merge_pdfs(self, pdf_files: List[Path]) -> bool:
        """Merge multiple PDFs into single file."""

        try:
            from PyPDF2 import PdfMerger
        except ImportError:
            print("ERROR: PyPDF2 required for PDF merging")
            print("Install: pip install PyPDF2")
            return False

        try:
            merger = PdfMerger()

            for pdf_file in pdf_files:
                merger.append(str(pdf_file))

            merger.write(str(self.output_path))
            merger.close()

            print(f"  ✓ Merged {len(pdf_files)} PDFs successfully")
            return True

        except Exception as e:
            print(f"ERROR during PDF merge: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Compile XHTML chapters into print-on-demand PDF"
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("REBRANDED_OUTPUT"),
        help="Source directory containing EPUB content (default: REBRANDED_OUTPUT)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("REBRANDED_OUTPUT/dist/The-Artisans-Path-POD.pdf"),
        help="Output PDF file path (default: REBRANDED_OUTPUT/dist/The-Artisans-Path-POD.pdf)"
    )
    parser.add_argument(
        "--targets",
        type=Path,
        help="Optional JSON file with chapter list (default: parse from content.opf)"
    )

    args = parser.parse_args()

    # Validate source exists
    if not args.source.exists():
        print(f"ERROR: Source directory not found: {args.source}")
        sys.exit(1)

    # Build PDF
    compiler = PDFCompiler(args.source, args.output, args.targets)
    success = compiler.compile_pdf()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
