#!/usr/bin/env python3
"""
Convert XHTML files to 6x9" Print-on-Demand PDFs
The Artisan's Path: Professional Hairstyling Excellence

Generates high-quality PDFs with embedded fonts for print-on-demand output.
"""

import os
import sys
from pathlib import Path
from weasyprint import HTML, CSS

# Paths
REPO_ROOT = Path("/root/repo")
XHTML_DIR = REPO_ROOT / "REBRANDED_OUTPUT" / "xhtml"
OUTPUT_DIR = REPO_ROOT / "pdf-pod"
STYLES_DIR = XHTML_DIR / "styles"

# CSS files to use (in order - cascade applies)
CSS_FILES = [
    STYLES_DIR / "style.css",
    STYLES_DIR / "print-pod.css"
]

# File definitions with categories
FILES = {
    "frontmatter": [
        "1-TitlePage.xhtml",
        "2-Copyright.xhtml",
        "3-TableOfContents.xhtml",
        "4-Dedication.xhtml",
        "5-SelfAssessment.xhtml",
        "6-AffirmationOdyssey.xhtml",
        "7-Preface.xhtml"
    ],
    "part-dividers": [
        "8-Part-I-Foundations-of-Creative-Hairstyling.xhtml",
        "12-Part-II-Building-Your-Professional-Practice.xhtml",
        "18-Part-III-Advanced-Business-Strategies.xhtml",
        "24-Part-IV-Future-Focused-Growth.xhtml"
    ],
    "chapters": [
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
    ],
    "backmatter": [
        "28-Conclusion.xhtml",
        "29-QuizKey.xhtml",
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
        "44-bibliography.xhtml"
    ]
}


def create_output_directories():
    """Create output directory structure."""
    for category in FILES.keys():
        (OUTPUT_DIR / category).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created output directories in {OUTPUT_DIR}")


def convert_file(xhtml_file, category):
    """Convert a single XHTML file to PDF."""
    input_path = XHTML_DIR / xhtml_file
    output_filename = xhtml_file.replace('.xhtml', '.pdf')
    output_path = OUTPUT_DIR / category / output_filename

    if not input_path.exists():
        print(f"  ✗ File not found: {xhtml_file}")
        return False

    try:
        # Load HTML
        html = HTML(filename=str(input_path))

        # Load CSS stylesheets
        css_objects = []
        for css_file in CSS_FILES:
            if css_file.exists():
                css_objects.append(CSS(filename=str(css_file)))
            else:
                print(f"  ⚠ CSS file not found: {css_file.name}")

        # Generate PDF
        html.write_pdf(
            target=str(output_path),
            stylesheets=css_objects,
            optimize_images=True
        )

        file_size = output_path.stat().st_size / 1024  # KB
        print(f"  ✓ {xhtml_file} → {output_filename} ({file_size:.1f} KB)")
        return True

    except Exception as e:
        print(f"  ✗ Error converting {xhtml_file}: {str(e)}")
        return False


def main():
    """Main conversion process."""
    print("="* 60)
    print("The Artisan's Path - 6x9\" POD PDF Converter")
    print("="* 60)
    print()

    # Create directories
    create_output_directories()
    print()

    # Track results
    total_files = sum(len(files) for files in FILES.values())
    successful = 0
    failed = 0

    # Convert files by category
    for category, file_list in FILES.items():
        print(f"Converting {category.upper()} ({len(file_list)} files):")
        print("-" * 60)

        for xhtml_file in file_list:
            if convert_file(xhtml_file, category):
                successful += 1
            else:
                failed += 1

        print()

    # Summary
    print("=" * 60)
    print("CONVERSION SUMMARY")
    print("=" * 60)
    print(f"Total files processed: {total_files}")
    print(f"Successful conversions: {successful}")
    print(f"Failed conversions: {failed}")
    print()
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Category breakdown
    print("Files by category:")
    for category in FILES.keys():
        count = len(list((OUTPUT_DIR / category).glob('*.pdf')))
        print(f"  {category}: {count} PDFs")

    print()
    print("✓ PDF conversion complete!")
    print()

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
