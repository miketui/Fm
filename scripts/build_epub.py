#!/usr/bin/env python3
"""
EPUB 3.2 Packaging Script for Professional Distribution

Compiles a valid EPUB file from REBRANDED_OUTPUT/ directory.
Follows EPUB 3.2 specification with proper compression and file ordering.

Usage:
    python3 scripts/build_epub.py --source REBRANDED_OUTPUT --output dist/book.epub
"""

import argparse
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime
from pathlib import Path
from typing import List, Tuple


class EPUBBuilder:
    """EPUB 3.2 packaging engine with validation."""

    def __init__(self, source_dir: Path, output_path: Path):
        self.source_dir = source_dir.resolve()
        self.output_path = output_path.resolve()
        self.temp_dir = None

    def validate_source(self) -> Tuple[bool, List[str]]:
        """Validate that source directory has all required EPUB components."""
        errors = []

        # Check required files
        required_files = [
            "mimetype",
            "META-INF/container.xml",
            "content.opf"
        ]

        for file_path in required_files:
            full_path = self.source_dir / file_path
            if not full_path.exists():
                errors.append(f"Missing required file: {file_path}")

        # Check mimetype content
        mimetype_path = self.source_dir / "mimetype"
        if mimetype_path.exists():
            content = mimetype_path.read_text().strip()
            if content != "application/epub+zip":
                errors.append(f"Invalid mimetype content: {content}")

        # Check for XHTML files
        xhtml_dir = self.source_dir / "xhtml"
        if not xhtml_dir.exists():
            errors.append("Missing xhtml directory")
        else:
            xhtml_files = list(xhtml_dir.glob("*.xhtml"))
            if len(xhtml_files) < 44:
                errors.append(f"Expected at least 44 XHTML files, found {len(xhtml_files)}")

        return (len(errors) == 0, errors)

    def build(self) -> bool:
        """Build EPUB file following EPUB 3.2 specification."""

        print(f"Building EPUB from: {self.source_dir}")
        print(f"Output: {self.output_path}")
        print()

        # Validate source
        print("[1/4] Validating source directory...")
        valid, errors = self.validate_source()
        if not valid:
            print("ERROR: Source validation failed:")
            for error in errors:
                print(f"  - {error}")
            return False
        print("  ✓ Source directory valid")

        # Create output directory
        print("\n[2/4] Preparing output directory...")
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        if self.output_path.exists():
            self.output_path.unlink()
        print(f"  ✓ Output directory ready")

        # Build EPUB ZIP
        print("\n[3/4] Packaging EPUB...")
        success = self._create_epub_zip()
        if not success:
            return False
        print(f"  ✓ EPUB packaged successfully")

        # Validate EPUB
        print("\n[4/4] Validating EPUB...")
        validation_result = self._validate_epub()

        # Report
        file_size = self.output_path.stat().st_size
        file_size_mb = file_size / (1024 * 1024)

        print("\n" + "=" * 60)
        print("EPUB BUILD COMPLETE")
        print("=" * 60)
        print(f"Output file: {self.output_path}")
        print(f"File size: {file_size_mb:.2f} MB")
        print(f"Validation: {'PASS' if validation_result else 'WARNINGS (see above)'}")
        print(f"Build time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)

        return True

    def _create_epub_zip(self) -> bool:
        """Create EPUB ZIP file with proper compression and ordering."""

        try:
            with zipfile.ZipFile(self.output_path, 'w') as epub_zip:

                # Step 1: Add mimetype (MUST be first, MUST be uncompressed)
                mimetype_path = self.source_dir / "mimetype"
                epub_zip.write(
                    mimetype_path,
                    arcname="mimetype",
                    compress_type=zipfile.ZIP_STORED  # No compression
                )
                print("    Added: mimetype (uncompressed)")

                # Step 2: Add META-INF directory
                meta_inf_dir = self.source_dir / "META-INF"
                for file_path in meta_inf_dir.rglob("*"):
                    if file_path.is_file():
                        arcname = file_path.relative_to(self.source_dir)
                        epub_zip.write(
                            file_path,
                            arcname=str(arcname),
                            compress_type=zipfile.ZIP_DEFLATED
                        )
                        print(f"    Added: {arcname}")

                # Step 3: Add content.opf
                content_opf = self.source_dir / "content.opf"
                epub_zip.write(
                    content_opf,
                    arcname="content.opf",
                    compress_type=zipfile.ZIP_DEFLATED
                )
                print("    Added: content.opf")

                # Step 4: Add all other files (XHTML, CSS, images, fonts)
                # Directories to completely exclude from EPUB (at any level)
                exclude_dirs = {
                    "pdf-pod", "templates", "react-components", "scripts",
                    "dist", ".claude", ".git", "__pycache__"
                }
                # Root-level directories to exclude (not subdirs like xhtml/styles)
                exclude_root_dirs = {"styles"}
                # File patterns to exclude
                exclude_extensions = {".md", ".MD", ".backup", ".bak", ".sh", ".py"}
                exclude_patterns = {"README", "TEMPLATE", "AUTOMATION", "SUMMARY", "GUIDE"}

                file_count = 0
                for file_path in sorted(self.source_dir.rglob("*")):
                    if file_path.is_file():
                        arcname = file_path.relative_to(self.source_dir)
                        arcname_str = str(arcname)
                        arcname_parts = arcname_str.split("/")

                        # Skip files in excluded directories
                        if any(part in exclude_dirs for part in arcname_parts):
                            continue
                        # Skip root-level excluded directories (e.g., "styles" but not "xhtml/styles")
                        if len(arcname_parts) >= 1 and arcname_parts[0] in exclude_root_dirs:
                            continue
                        # Skip files with excluded extensions
                        if any(arcname_str.endswith(ext) for ext in exclude_extensions):
                            continue
                        # Skip files matching excluded patterns
                        if any(pattern in arcname_str for pattern in exclude_patterns):
                            continue

                        # Skip already added files
                        if str(arcname) in ["mimetype", "content.opf"]:
                            continue
                        if str(arcname).startswith("META-INF"):
                            continue

                        # Add file
                        epub_zip.write(
                            file_path,
                            arcname=str(arcname),
                            compress_type=zipfile.ZIP_DEFLATED
                        )
                        file_count += 1

                        # Log every 10th file to avoid spam
                        if file_count % 10 == 0:
                            print(f"    Added {file_count} files...")

                print(f"    ✓ Total files added: {file_count + 3}")  # +3 for mimetype, META-INF/*, content.opf

            return True

        except Exception as e:
            print(f"ERROR during ZIP creation: {e}")
            return False

    def _validate_epub(self) -> bool:
        """Validate EPUB using EPUBCheck if available."""

        epubcheck_cmd = shutil.which("epubcheck")
        if not epubcheck_cmd:
            print("  ⚠ EPUBCheck not found - skipping validation")
            print("    Install from: https://github.com/w3c/epubcheck")
            return False

        try:
            result = subprocess.run(
                [epubcheck_cmd, str(self.output_path)],
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print("  ✓ EPUBCheck validation PASSED")
                return True
            else:
                print("  ⚠ EPUBCheck found issues:")
                print(result.stdout)
                if result.stderr:
                    print(result.stderr)
                return False

        except subprocess.TimeoutExpired:
            print("  ⚠ EPUBCheck validation timed out")
            return False
        except Exception as e:
            print(f"  ⚠ EPUBCheck validation error: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Build professional EPUB 3.2 file for distribution"
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
        default=Path("REBRANDED_OUTPUT/dist/The-Artisans-Path.epub"),
        help="Output EPUB file path (default: REBRANDED_OUTPUT/dist/The-Artisans-Path.epub)"
    )

    args = parser.parse_args()

    # Validate source exists
    if not args.source.exists():
        print(f"ERROR: Source directory not found: {args.source}")
        sys.exit(1)

    # Build EPUB
    builder = EPUBBuilder(args.source, args.output)
    success = builder.build()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
