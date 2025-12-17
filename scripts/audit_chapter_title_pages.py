#!/usr/bin/env python3
"""
Audit Chapter Title Page Consistency
Verifies all 16 chapters follow the standard design pattern
"""

import re
import sys
from pathlib import Path
from typing import Any, Dict, List

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

CHAPTER_FILES = [
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
    "27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml",
]

EXPECTED_PATTERN = {
    "chapter-title-shell": "Main container section",
    "chapter-opening-quote": "Opening quote with left border",
    "quote-text": "Quote text content",
    "quote-citation": "Quote citation",
    "chapter-number-badge": "Circular badge with Roman numeral",
    "decorative-divider": "Gold divider line",
    "chapter-title": "Chapter title text",
    "chapter-introduction-quote": "Introduction quote section",
    "introduction-heading": "Introduction heading",
    "introduction-paragraph": "Opening paragraph with drop cap",
}

def check_chapter_structure(filepath: Path) -> Dict[str, Any]:
    """Check if chapter has all required structural elements"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    results = {
        "file": filepath.name,
        "passed": True,
        "missing_classes": [],
        "found_classes": {},
        "warnings": [],
        "errors": []
    }

    # Check for required CSS classes
    for css_class, description in EXPECTED_PATTERN.items():
        pattern = rf'class="[^"]*{re.escape(css_class)}[^"]*"'
        matches = re.findall(pattern, content)

        if matches:
            results["found_classes"][css_class] = len(matches)
        else:
            results["missing_classes"].append(css_class)
            results["passed"] = False
            results["errors"].append(f"Missing class: {css_class} ({description})")

    # Check for chapter number badge (Roman numeral)
    if not re.search(r'class="[^"]*chapter-number[^"]*"[^>]*>[IVXLCDM]+<', content):
        results["warnings"].append("Chapter number (Roman numeral) not found in badge")

    # Check for opening quote image
    if not re.search(r'<img[^>]+chapter-[ivxlcdm]+-quote\.jpeg', content):
        results["warnings"].append("Opening quote image not found")

    # Check for drop cap styling
    if not re.search(r'class="[^"]*drop-cap[^"]*"', content):
        results["warnings"].append("Drop cap styling not found in opening paragraph")

    # Check for gold-accent class (left border)
    gold_accent_count = len(re.findall(r'class="[^"]*gold-accent[^"]*"', content))
    if gold_accent_count < 2:
        results["warnings"].append(f"Expected at least 2 gold-accent borders, found {gold_accent_count}")

    # Check for Introduction heading
    if not re.search(r'<h2[^>]*class="[^"]*introduction-heading[^"]*"[^>]*>Introduction</h2>', content):
        results["warnings"].append("'Introduction' heading not found or incorrectly formatted")

    return results


def generate_report(audit_results: List[Dict]) -> None:
    """Generate formatted audit report"""

    print(f"\n{'='*80}")
    print(f"{BLUE}CHAPTER TITLE PAGE CONSISTENCY AUDIT{RESET}")
    print(f"{'='*80}\n")

    passed_count = sum(1 for r in audit_results if r["passed"] and not r["warnings"])
    warning_count = sum(1 for r in audit_results if r["warnings"])
    failed_count = sum(1 for r in audit_results if not r["passed"])

    print(f"Total Chapters: {len(audit_results)}")
    print(f"{GREEN}✓ Perfect:{RESET} {passed_count}")
    print(f"{YELLOW}⚠ Warnings:{RESET} {warning_count}")
    print(f"{RED}✗ Failed:{RESET} {failed_count}\n")

    # Detailed results
    for result in audit_results:
        if result["passed"] and not result["warnings"]:
            status = f"{GREEN}✓ PASS{RESET}"
        elif result["warnings"]:
            status = f"{YELLOW}⚠ WARN{RESET}"
        else:
            status = f"{RED}✗ FAIL{RESET}"

        print(f"{status} | {result['file']}")

        if result["errors"]:
            for error in result["errors"]:
                print(f"      {RED}ERROR:{RESET} {error}")

        if result["warnings"]:
            for warning in result["warnings"]:
                print(f"      {YELLOW}WARN:{RESET} {warning}")

        if result["found_classes"]:
            class_summary = ", ".join([f"{k}({v})" for k, v in result["found_classes"].items()])
            if len(class_summary) > 60:
                class_summary = class_summary[:57] + "..."
            print(f"      {BLUE}INFO:{RESET} Found classes: {class_summary}")

        print()

    # Summary statistics
    print(f"\n{'='*80}")
    print(f"{BLUE}PATTERN ELEMENT COVERAGE{RESET}")
    print(f"{'='*80}\n")

    for css_class, description in EXPECTED_PATTERN.items():
        found_in = sum(1 for r in audit_results if css_class in r["found_classes"])
        coverage = (found_in / len(audit_results)) * 100

        if coverage == 100:
            status = f"{GREEN}100%{RESET}"
        elif coverage >= 80:
            status = f"{YELLOW}{coverage:.0f}%{RESET}"
        else:
            status = f"{RED}{coverage:.0f}%{RESET}"

        print(f"{status} | {css_class:<30} | {description}")

    print(f"\n{'='*80}\n")

    # Final verdict
    if failed_count == 0 and warning_count == 0:
        print(f"{GREEN}✓ ALL CHAPTERS PASS CONSISTENCY CHECK{RESET}")
        print(f"All 16 chapters follow the standard title page design pattern.\n")
        return 0
    elif failed_count == 0:
        print(f"{YELLOW}⚠ CHAPTERS PASS WITH WARNINGS{RESET}")
        print(f"All chapters have required structure, but {warning_count} have minor inconsistencies.\n")
        return 1
    else:
        print(f"{RED}✗ CONSISTENCY CHECK FAILED{RESET}")
        print(f"{failed_count} chapter(s) missing required structural elements.\n")
        return 2


def main():
    """Main audit execution"""

    root_dir = Path(__file__).resolve().parent.parent / "REBRANDED_OUTPUT" / "xhtml"

    if not root_dir.exists():
        print(f"{RED}ERROR:{RESET} REBRANDED_OUTPUT/xhtml/ directory not found")
        return 1

    audit_results = []

    for chapter_file in CHAPTER_FILES:
        filepath = root_dir / chapter_file

        if not filepath.exists():
            audit_results.append({
                "file": chapter_file,
                "passed": False,
                "missing_classes": list(EXPECTED_PATTERN.keys()),
                "found_classes": {},
                "warnings": [],
                "errors": [f"File not found: {filepath}"]
            })
            continue

        result = check_chapter_structure(filepath)
        audit_results.append(result)

    exit_code = generate_report(audit_results)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
