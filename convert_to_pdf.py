#!/usr/bin/env python3
"""
Convert all XHTML files to PDF using wkhtmltopdf
"""

import os
import subprocess
import sys
from pathlib import Path

def convert_xhtml_to_pdf():
    """Convert all XHTML files in output/OEBPS/text/ to PDF"""

    # Setup paths
    base_dir = Path("/workspace/Fm")
    input_dir = base_dir / "output" / "OEBPS" / "text"
    output_dir = base_dir / "pdf"

    # Ensure output directory exists
    output_dir.mkdir(exist_ok=True)

    # Find all XHTML files
    xhtml_files = list(input_dir.glob("*.xhtml"))

    if not xhtml_files:
        print("No XHTML files found!")
        return

    # Sort files by name for consistent processing
    xhtml_files.sort()

    print(f"Found {len(xhtml_files)} XHTML files to convert")

    successful = 0
    failed = 0

    for xhtml_file in xhtml_files:
        # Create output PDF filename
        pdf_filename = xhtml_file.stem + ".pdf"
        pdf_path = output_dir / pdf_filename

        # Full path for wkhtmltopdf
        input_url = f"file://{xhtml_file.absolute()}"

        # wkhtmltopdf command
        cmd = [
            "wkhtmltopdf",
            "--page-size", "A4",
            "--margin-top", "20mm",
            "--margin-bottom", "20mm",
            "--margin-left", "20mm",
            "--margin-right", "20mm",
            "--enable-local-file-access",
            "--quiet",  # Reduce output noise
            input_url,
            str(pdf_path)
        ]

        try:
            # Run conversion
            print(f"Converting: {xhtml_file.name} -> {pdf_filename}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            if result.returncode == 0:
                successful += 1
                print(f"  ✓ Success: {pdf_filename}")
            else:
                failed += 1
                print(f"  ✗ Failed: {pdf_filename}")
                if result.stderr:
                    print(f"    Error: {result.stderr.strip()}")

        except subprocess.TimeoutExpired:
            failed += 1
            print(f"  ✗ Timeout: {pdf_filename}")
        except Exception as e:
            failed += 1
            print(f"  ✗ Exception: {pdf_filename} - {e}")

    print(f"\nConversion complete:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(xhtml_files)}")

    # List generated PDFs
    pdf_files = list(output_dir.glob("*.pdf"))
    if pdf_files:
        print(f"\nGenerated PDFs in {output_dir}:")
        for pdf_file in sorted(pdf_files):
            size_mb = pdf_file.stat().st_size / 1024 / 1024
            print(f"  {pdf_file.name} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    convert_xhtml_to_pdf()