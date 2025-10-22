#!/usr/bin/env python3
"""
XHTML Refactoring Script for EPUB Production
Refactors all 45 XHTML files to match ACISS templates while preserving 100% of content.
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple
import shutil
from datetime import datetime

# Namespace definitions
XHTML_NS = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
ET.register_namespace('', XHTML_NS)
ET.register_namespace('epub', EPUB_NS)

class XHTMLRefactor:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.text_dir = self.base_dir / "OEBPS" / "text"
        self.templates_dir = self.base_dir / "templates"
        self.backup_dir = self.base_dir / "backups" / f"xhtml_refactor_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # File classification
        self.frontmatter_files = [
            "1-TitlePage.xhtml",
            "2-Copyright.xhtml",
            "3-TableOfContents.xhtml",
            "4-Dedication.xhtml",
            "5-SelfAssessment.xhtml",
            "6-affirmation-odyssey.xhtml",
            "7-Preface.xhtml"
        ]
        
        self.part_files = [
            "8-Part-I-Foundations-of-Creative-Hairstyling.xhtml",
            "12-Part-II-Building-Your-Professional-Practice.xhtml",
            "18-Part-III-Advanced-Business-Strategies.xhtml",
            "24-Part-IV-Future-Focused-Growth.xhtml"
        ]
        
        self.chapter_files = [
            "9-chapter-i-unveiling-your-creative-odyssey.xhtml",
            "10-chapter-ii-refining-your-creative-toolkit.xhtml",
            "11-chapter-iii-reigniting-your-creative-fire.xhtml",
            "13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml",
            "14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml",
            "15-chapter-vi-mastering-the-business-of-hairstyling.xhtml",
            "16-chapter-vii-embracing-wellness-and-self-care.xhtml",
            "17-chapter-viii-advancing-skills-through-continuous-education.xhtml",
            "19-chapter-ix-stepping-into-leadership.xhtml",
            "20-chapter-x-crafting-enduring-legacies.xhtml",
            "21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml",
            "22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml",
            "23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml",
            "25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml",
            "26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml",
            "27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml"
        ]
        
        self.backmatter_files = [
            "28-Conclusion.xhtml",
            "29QuizKey.xhtml",
            "30-SelfAssessment.xhtml",
            "31-affirmations-close.xhtml",
            "32-continued-learning-commitment.xhtml",
            "33-Acknowledgments.xhtml",
            "34-AbouttheAuthor.xhtml",
            "35-CurlsContempCollective.xhtml",
            "36-JournalingStart.xhtml",
            "37-ManifestingJournal.xhtml",
            "38-journal-page.xhtml",
            "39-professional-development.xhtml",
            "40-SMARTGoals.xhtml",
            "41-self-care-journal.xhtml",
            "42-VisionJournal.xhtml",
            "43-DoodlePage.xhtml",
            "44-bibliography.xhtml",
            "nav.xhtml"
        ]

    def backup_files(self):
        """Create backup of all XHTML files before processing"""
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        for file in self.text_dir.glob("*.xhtml"):
            shutil.copy2(file, self.backup_dir / file.name)
        print(f"✓ Backed up {len(list(self.backup_dir.glob('*.xhtml')))} files to {self.backup_dir}")

    def read_file_content(self, filepath: Path) -> str:
        """Read file content preserving encoding"""
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def write_file_content(self, filepath: Path, content: str):
        """Write file content preserving encoding"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def extract_text_content(self, content: str) -> str:
        """Extract main text content from XHTML, preserving all text nodes"""
        # Remove XML declaration and DOCTYPE if present
        content = re.sub(r'<\?xml[^>]*\?>', '', content)
        content = re.sub(r'<!DOCTYPE[^>]*>', '', content)
        return content.strip()

    def validate_xhtml(self, filepath: Path) -> bool:
        """Validate XHTML file is well-formed"""
        try:
            tree = ET.parse(filepath)
            return True
        except ET.ParseError as e:
            print(f"✗ Validation error in {filepath.name}: {e}")
            return False

    def count_words(self, text: str) -> int:
        """Count words in text content"""
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        words = text.split()
        return len(words)

    def remove_inline_styles(self, content: str) -> str:
        """Remove inline <style> blocks from XHTML content"""
        # Remove <style>...</style> blocks
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
        # Remove inline style attributes
        content = re.sub(r'\s+style="[^"]*"', '', content)
        return content

    def normalize_head(self, content: str, title: str, lang: str = "en") -> str:
        """Normalize the <head> section to match template standards"""
        # Extract existing head content
        head_match = re.search(r'<head[^>]*>(.*?)</head>', content, re.DOTALL)
        if not head_match:
            return content
        
        # Create new standardized head
        new_head = f'''<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title}</title>
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/print.css" media="print"/>
</head>'''
        
        # Replace head section
        content = re.sub(r'<head[^>]*>.*?</head>', new_head, content, flags=re.DOTALL)
        return content

    def normalize_html_tag(self, content: str, lang: str = "en") -> str:
        """Normalize the <html> tag to include proper namespaces and lang attributes"""
        # Standard XHTML/EPUB html tag
        new_html_tag = f'<html xmlns="{XHTML_NS}" xmlns:epub="{EPUB_NS}" lang="{lang}" xml:lang="{lang}">'
        
        # Replace html tag
        content = re.sub(r'<html[^>]*>', new_html_tag, content)
        return content

    def normalize_body_class(self, content: str, file_type: str) -> str:
        """Normalize body class based on file type"""
        # Define correct body classes per type
        class_map = {
            'frontmatter': 'frontmatter-page',
            'part': 'part-page',
            'chapter': 'chapter-page',
            'backmatter': 'backmatter-page'
        }
        
        correct_class = class_map.get(file_type, 'page')
        
        # Replace body tag with correct class
        content = re.sub(r'<body[^>]*>', f'<body class="{correct_class}">', content)
        
        # Remove wrapper divs that are not needed (like <div class="single-page ...">)
        # Keep the actual content but remove unnecessary wrapper divs
        if file_type in ['frontmatter', 'backmatter']:
            # Remove opening wrapper divs after body
            content = re.sub(r'(<body[^>]*>)\s*<div[^>]*class="[^"]*(?:single-page|backmatter-page)[^"]*"[^>]*>', r'\1', content)
            # Remove closing wrapper divs before </body>
            content = re.sub(r'</div>\s*</body>', '</body>', content)
        
        return content

    def refactor_file(self, filename: str, file_type: str) -> bool:
        """
        Refactor a single XHTML file based on its type.
        Returns True if successful, False otherwise.
        """
        filepath = self.text_dir / filename
        
        if not filepath.exists():
            print(f"✗ File not found: {filename}")
            return False

        print(f"\nProcessing: {filename} (type: {file_type})")
        
        try:
            # Read original content
            original_content = self.read_file_content(filepath)
            original_word_count = self.count_words(original_content)
            
            # Extract title
            title_match = re.search(r'<title>([^<]+)</title>', original_content)
            title = title_match.group(1) if title_match else filename.replace('.xhtml', '')
            
            # Remove inline styles
            cleaned_content = self.remove_inline_styles(original_content)
            
            # Normalize HTML tag
            cleaned_content = self.normalize_html_tag(cleaned_content)
            
            # Normalize head section
            cleaned_content = self.normalize_head(cleaned_content, title)
            
            # Normalize body class and structure
            cleaned_content = self.normalize_body_class(cleaned_content, file_type)
            
            # Verify word count preservation
            new_word_count = self.count_words(cleaned_content)
            
            # Allow small variance due to style removal
            word_diff = abs(original_word_count - new_word_count)
            if word_diff > 5:  # More than 5 words difference is suspicious
                print(f"  ⚠ Word count changed: {original_word_count} -> {new_word_count} (diff: {word_diff})")
            
            # Write cleaned content back
            self.write_file_content(filepath, cleaned_content)
            
            # Validate the result
            if self.validate_xhtml(filepath):
                print(f"  ✓ Refactored successfully (words: {new_word_count})")
                return True
            else:
                # Restore from backup if validation fails
                backup_file = self.backup_dir / filename
                shutil.copy2(backup_file, filepath)
                print(f"  ✗ Validation failed - restored from backup")
                return False
                
        except Exception as e:
            print(f"✗ Error processing {filename}: {e}")
            import traceback
            traceback.print_exc()
            # Restore from backup on error
            backup_file = self.backup_dir / filename
            if backup_file.exists():
                shutil.copy2(backup_file, filepath)
                print(f"  ↻ Restored from backup")
            return False

    def process_all_files(self):
        """Process all 45 XHTML files"""
        stats = {
            'frontmatter': 0,
            'part': 0,
            'chapter': 0,
            'backmatter': 0,
            'failed': 0
        }
        
        print("\n" + "="*70)
        print("XHTML REFACTORING - ACISS Template Normalization")
        print("="*70)
        
        # Process frontmatter files
        print("\n--- FRONTMATTER FILES (7 files) ---")
        for filename in self.frontmatter_files:
            if self.refactor_file(filename, 'frontmatter'):
                stats['frontmatter'] += 1
            else:
                stats['failed'] += 1
        
        # Process part divider files
        print("\n--- PART DIVIDER FILES (4 files) ---")
        for filename in self.part_files:
            if self.refactor_file(filename, 'part'):
                stats['part'] += 1
            else:
                stats['failed'] += 1
        
        # Process chapter files
        print("\n--- CHAPTER FILES (16 files) ---")
        for filename in self.chapter_files:
            if self.refactor_file(filename, 'chapter'):
                stats['chapter'] += 1
            else:
                stats['failed'] += 1
        
        # Process backmatter files
        print("\n--- BACKMATTER FILES (18 files) ---")
        for filename in self.backmatter_files:
            if self.refactor_file(filename, 'backmatter'):
                stats['backmatter'] += 1
            else:
                stats['failed'] += 1
        
        # Print summary
        print("\n" + "="*70)
        print("SUMMARY")
        print("="*70)
        print(f"Frontmatter: {stats['frontmatter']}/{len(self.frontmatter_files)}")
        print(f"Part Dividers: {stats['part']}/{len(self.part_files)}")
        print(f"Chapters: {stats['chapter']}/{len(self.chapter_files)}")
        print(f"Backmatter: {stats['backmatter']}/{len(self.backmatter_files)}")
        print(f"Failed: {stats['failed']}")
        total_processed = stats['frontmatter'] + stats['part'] + stats['chapter'] + stats['backmatter']
        print(f"\nTotal: {total_processed}/45 files processed successfully")
        
        return stats['failed'] == 0


def main():
    """Main execution function"""
    base_dir = "/home/runner/work/Fm/Fm"
    refactor = XHTMLRefactor(base_dir)
    
    # Create backup first
    refactor.backup_files()
    
    # Process all files
    success = refactor.process_all_files()
    
    if success:
        print("\n✓ All files processed successfully!")
        return 0
    else:
        print("\n✗ Some files failed processing. Check errors above.")
        return 1


if __name__ == "__main__":
    exit(main())
