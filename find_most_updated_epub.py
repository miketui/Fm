#!/usr/bin/env python3
"""
Find the most updated EPUB file in REBRANDED_OUTPUT directory.

This script analyzes all EPUB files in the REBRANDED_OUTPUT/dist directory,
checks their validity, size, and modification time, and reports which one
is the most recently updated and production-ready.

Usage:
    python3 find_most_updated_epub.py
"""

import os
import sys
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class EPUBAnalyzer:
    """Analyze EPUB files to determine the most updated version."""

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.dist_dir = base_dir / "dist"

    def is_valid_epub(self, epub_path: Path) -> Tuple[bool, str]:
        """
        Check if a file is a valid EPUB.
        
        Returns:
            Tuple of (is_valid, reason)
        """
        # Check file size
        file_size = epub_path.stat().st_size
        if file_size < 100:
            return False, f"File too small ({file_size} bytes) - likely corrupted"

        # Check if it's a valid ZIP file
        try:
            with zipfile.ZipFile(epub_path, 'r') as zip_file:
                # Check for mimetype file
                if 'mimetype' not in zip_file.namelist():
                    return False, "Missing mimetype file"
                
                # Check mimetype content
                mimetype_content = zip_file.read('mimetype').decode('utf-8').strip()
                if mimetype_content != 'application/epub+zip':
                    return False, f"Invalid mimetype: {mimetype_content}"
                
                # Check for required EPUB files
                if 'META-INF/container.xml' not in zip_file.namelist():
                    return False, "Missing META-INF/container.xml"
                
                # Check for content.opf
                opf_files = [f for f in zip_file.namelist() if f.endswith('.opf')]
                if not opf_files:
                    return False, "Missing .opf package file"
                
                return True, "Valid EPUB structure"
        except zipfile.BadZipFile:
            return False, "Not a valid ZIP file"
        except Exception as e:
            return False, f"Error reading file: {str(e)}"

    def get_epub_info(self, epub_path: Path) -> Dict:
        """
        Get detailed information about an EPUB file.
        
        Returns:
            Dictionary with EPUB metadata and stats
        """
        info = {
            'filename': epub_path.name,
            'path': str(epub_path),
            'size_bytes': epub_path.stat().st_size,
            'size_mb': epub_path.stat().st_size / (1024 * 1024),
            'modified_time': datetime.fromtimestamp(epub_path.stat().st_mtime),
            'is_valid': False,
            'validation_message': '',
            'file_count': 0,
            'xhtml_count': 0,
            'image_count': 0,
        }

        # Validate EPUB
        is_valid, message = self.is_valid_epub(epub_path)
        info['is_valid'] = is_valid
        info['validation_message'] = message

        # If valid, get more details
        if is_valid:
            try:
                with zipfile.ZipFile(epub_path, 'r') as zip_file:
                    all_files = zip_file.namelist()
                    info['file_count'] = len(all_files)
                    info['xhtml_count'] = len([f for f in all_files if f.endswith('.xhtml')])
                    info['image_count'] = len([f for f in all_files 
                                              if any(f.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg'])])
            except Exception as e:
                info['validation_message'] += f" (Warning: Could not read file details: {str(e)})"

        return info

    def find_all_epubs(self) -> List[Path]:
        """Find all EPUB files in the dist directory."""
        if not self.dist_dir.exists():
            return []
        
        return sorted(self.dist_dir.glob("*.epub"))

    def analyze_all_epubs(self) -> List[Dict]:
        """Analyze all EPUB files and return their information."""
        epub_files = self.find_all_epubs()
        
        if not epub_files:
            return []
        
        return [self.get_epub_info(epub) for epub in epub_files]

    def find_most_updated(self) -> Optional[Dict]:
        """
        Find the most updated, valid EPUB file.
        
        Prioritizes based on content version significance:
        1. "Normalized-v2" versions (most recent content updates per documentation)
        2. "Normalized" versions (intermediate updates)
        3. Standard production version
        4. Then by modification time and file size
        """
        all_epubs = self.analyze_all_epubs()
        
        # Filter to only valid EPUBs
        valid_epubs = [epub for epub in all_epubs if epub['is_valid']]
        
        if not valid_epubs:
            return None
        
        # Define priority scoring for filenames based on documentation
        def get_priority_score(epub):
            filename = epub['filename']
            score = 0
            
            # Highest priority: Normalized-v2 (latest content iteration per docs/FINAL_NORMALIZATION_SUMMARY.md)
            if 'Normalized-v2' in filename:
                score = 1000
            # Medium priority: Normalized (first iteration per docs/NORMALIZATION_VALIDATION_REPORT.md)
            elif 'Normalized' in filename:
                score = 500
            # Standard priority: The-Artisans-Path (production version per docs/DISTRIBUTION_PACKAGE_REPORT.md)
            elif filename == 'The-Artisans-Path.epub':
                score = 100
            # Lower priority for other variants
            else:
                score = 10
            
            return score
        
        # Sort by priority score (descending), then by modification time (descending), then by size (descending)
        # This ensures we get the most content-complete version regardless of file timestamp
        valid_epubs.sort(key=lambda x: (get_priority_score(x), x['modified_time'], x['size_bytes']), reverse=True)
        
        return valid_epubs[0]

    def print_report(self):
        """Print a detailed report of all EPUB files."""
        print("=" * 80)
        print("EPUB ANALYSIS REPORT - REBRANDED_OUTPUT")
        print("=" * 80)
        print()
        
        all_epubs = self.analyze_all_epubs()
        
        if not all_epubs:
            print("❌ No EPUB files found in REBRANDED_OUTPUT/dist/")
            return
        
        print(f"📁 Directory: {self.dist_dir}")
        print(f"📚 Total EPUB files found: {len(all_epubs)}")
        print()
        
        # Print details for each EPUB
        print("─" * 80)
        print("ALL EPUB FILES:")
        print("─" * 80)
        
        for epub in all_epubs:
            status = "✅ VALID" if epub['is_valid'] else "❌ INVALID"
            print(f"\n{status} - {epub['filename']}")
            print(f"  Path: {epub['path']}")
            print(f"  Size: {epub['size_mb']:.2f} MB ({epub['size_bytes']:,} bytes)")
            print(f"  Modified: {epub['modified_time'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"  Status: {epub['validation_message']}")
            
            if epub['is_valid']:
                print(f"  Contents: {epub['file_count']} files total")
                print(f"            {epub['xhtml_count']} XHTML files")
                print(f"            {epub['image_count']} image files")
        
        print()
        print("=" * 80)
        print("MOST UPDATED EPUB")
        print("=" * 80)
        
        most_updated = self.find_most_updated()
        
        if not most_updated:
            print("\n❌ No valid EPUB files found!")
            print("\nAll EPUB files in the directory are either corrupted or invalid.")
            return
        
        print(f"\n✅ RECOMMENDED FILE: {most_updated['filename']}")
        print()
        print(f"📄 Filename: {most_updated['filename']}")
        print(f"📍 Path: {most_updated['path']}")
        print(f"📦 Size: {most_updated['size_mb']:.2f} MB")
        print(f"🕐 Last Modified: {most_updated['modified_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"✓ Validation: {most_updated['validation_message']}")
        print(f"📊 Contents:")
        print(f"   - Total files: {most_updated['file_count']}")
        print(f"   - XHTML chapters: {most_updated['xhtml_count']}")
        print(f"   - Images: {most_updated['image_count']}")
        print()
        
        # Provide context based on filename
        if "Normalized-v2" in most_updated['filename']:
            print("ℹ️  CONTENT VERSION: 'Normalized v2' (Latest Complete Edition)")
            print()
            print("   This is the most content-complete version with:")
            print("   ✓ Fixed drop-cap styling in Chapter I (no double drop-cap)")
            print("   ✓ Complete backmatter worksheets (not placeholders)")
            print("     - Self-Care Journal (41-self-care-journal.xhtml)")
            print("     - Vision Journal (42-VisionJournal.xhtml)")
            print("     - Journal Page (38-journal-page.xhtml)")
            print("     - Creative Doodle Page (43-DoodlePage.xhtml)")
            print("   ✓ Proper page breaks for all chapters")
            print("   ✓ All 46 XHTML files with full content")
            print()
            print("   Documentation: docs/FINAL_NORMALIZATION_SUMMARY.md")
        elif "Normalized" in most_updated['filename']:
            print("ℹ️  CONTENT VERSION: 'Normalized' (First Iteration)")
            print()
            print("   This is the first normalized edition.")
            print("   Note: The 'Normalized-v2' version contains additional fixes.")
        elif most_updated['filename'] == "The-Artisans-Path.epub":
            print("ℹ️  CONTENT VERSION: Standard Production EPUB")
            print()
            print("   This is the standard production EPUB for distribution.")
            print("   See REBRANDED_OUTPUT/dist/README.md for distribution info.")
        elif most_updated['filename'] == "curls.epub":
            print("ℹ️  CONTENT VERSION: Alternative build")
            print()
            print("   This appears to be an alternative build with different")
            print("   chapter organization (62 XHTML files vs. standard 46).")
        
        print()
        print("=" * 80)
        print()


def main():
    """Main entry point for the script."""
    # Find the REBRANDED_OUTPUT directory
    current_dir = Path.cwd()
    rebranded_output = current_dir / "REBRANDED_OUTPUT"
    
    if not rebranded_output.exists():
        print(f"❌ ERROR: REBRANDED_OUTPUT directory not found at {rebranded_output}")
        print()
        print("This script should be run from the repository root directory.")
        sys.exit(1)
    
    # Create analyzer and run report
    analyzer = EPUBAnalyzer(rebranded_output)
    analyzer.print_report()
    
    # Exit with success code if we found a valid EPUB
    most_updated = analyzer.find_most_updated()
    sys.exit(0 if most_updated else 1)


if __name__ == "__main__":
    main()