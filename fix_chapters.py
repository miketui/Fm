#!/usr/bin/env python3
"""Safely align chapter XHTML structure without altering prose."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, Iterable, List

CHAPTERS = [
    ("9-chapter-i-unveiling-your-creative-odyssey.xhtml", "chapter-i-quote.jpeg"),
    ("10-chapter-ii-refining-your-creative-toolkit.xhtml", "chapter-ii-quote.jpeg"),
    ("11-chapter-iii-reigniting-your-creative-fire.xhtml", "chapter-iii-quote.jpeg"),
    ("13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml", "chapter-iv-quote.jpeg"),
    ("14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml", "chapter-v-quote.jpeg"),
    ("15-chapter-vi-mastering-the-business-of-hairstyling.xhtml", "chapter-vi-quote.jpeg"),
    ("16-chapter-vii-embracing-wellness-and-self-care.xhtml", "chapter-vii-quote.jpeg"),
    ("17-chapter-viii-advancing-skills-through-continuous-education.xhtml", "chapter-viii-quote.jpeg"),
    ("19-chapter-ix-stepping-into-leadership.xhtml", "chapter-ix-quote.jpeg"),
    ("20-chapter-x-crafting-enduring-legacies.xhtml", "chapter-x-quote.jpeg"),
    ("21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml", "chapter-xi-quote.jpeg"),
    ("22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml", "chapter-xii-quote.jpeg"),
    ("23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml", "chapter-xiii-quote.jpeg"),
    ("25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml", "chapter-xiv-quote.jpeg"),
    ("26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml", "chapter-xv-quote.jpeg"),
    ("27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml", "chapter-xvi-quote.jpeg"),
]

STYLE_BLOCK = """
    <style>
    .page-break-before {
        page-break-before: always;
        break-before: page;
    }
    .page-break-after {
        page-break-after: always;
        break-after: page;
    }
    .avoid-break {
        page-break-inside: avoid;
        break-inside: avoid;
    }
    .quiz-container {
        max-height: 90vh;
        padding: 20px;
        margin-bottom: 0;
    }
    .worksheet {
        max-height: 90vh;
        padding: 20px;
        margin-top: 0;
    }
    .quote-page {
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 90vh;
        page-break-before: always;
        break-before: page;
    }
    .quote-page img {
        max-width: 80%;
        max-height: 70vh;
        object-fit: contain;
    }
    </style>
"""


class TextExtractor(HTMLParser):
    """Collect word tokens from XHTML content for fidelity checks."""

    def __init__(self) -> None:
        super().__init__()
        self.tokens: List[str] = []

    def handle_data(self, data: str) -> None:  # noqa: D401 - HTMLParser hook
        words = data.split()
        if words:
            self.tokens.extend(words)

    def get_tokens(self) -> List[str]:
        return self.tokens


def extract_tokens(xhtml: str) -> List[str]:
    parser = TextExtractor()
    parser.feed(xhtml)
    parser.close()
    return parser.get_tokens()


def insert_attribute(tag: str, attribute: str, value: str) -> str:
    ending = "/>" if tag.rstrip().endswith("/>") else ">"
    core = tag.rstrip().removesuffix(ending)
    return f"{core} {attribute}=\"{value}\"{ending}"


def add_classes(tag: str, classes: Iterable[str]) -> str:
    class_pattern = re.compile(r'class="([^"]*)"', re.IGNORECASE)
    match = class_pattern.search(tag)
    if match:
        existing = match.group(1).split()
    else:
        existing = []
    updated = list(existing)
    for cls in classes:
        if cls not in updated:
            updated.append(cls)
    updated_classes = " ".join(updated)
    if match:
        return class_pattern.sub(f'class="{updated_classes}"', tag, count=1)
    return insert_attribute(tag, "class", updated_classes)


def set_attribute(tag: str, attribute: str, value: str) -> str:
    pattern = re.compile(rf'\s{attribute}="[^"]*"', re.IGNORECASE)
    if pattern.search(tag):
        return pattern.sub(f' {attribute}="{value}"', tag, count=1)
    return insert_attribute(tag, attribute, value)


def add_page_break_styles(content: str) -> str:
    if STYLE_BLOCK.strip() in content:
        return content
    return content.replace("</head>", f"{STYLE_BLOCK}</head>")


def ensure_section_attributes(content: str, target_class: str, classes: Iterable[str], attributes: Dict[str, str]) -> str:
    pattern = re.compile(r'(<section[^>]*class="[^"]*\b' + re.escape(target_class) + r'\b[^"]*"[^>]*>)', re.IGNORECASE)

    def replacer(match: re.Match[str]) -> str:
        tag = match.group(1)
        tag = add_classes(tag, classes)
        for attr, value in attributes.items():
            tag = set_attribute(tag, attr, value)
        return tag

    return pattern.sub(replacer, content)


def add_page_break_after_endnotes(content: str) -> str:
    return content.replace('class="endnotes"', 'class="endnotes page-break-after"')


def update_quote_image(content: str, image_file: str, current_file: Path) -> str:
    section_pattern = re.compile(r'(<section[^>]*class="[^"]*\bquote-page\b[^"]*"[^>]*>.*?</section>)', re.IGNORECASE | re.DOTALL)
    img_pattern = re.compile(r'(<img[^>]*>)', re.IGNORECASE)

    def section_replacer(match: re.Match[str]) -> str:
        section_html = match.group(1)

        def img_replacer(img_match: re.Match[str]) -> str:
            img_tag = img_match.group(1)
            updated_tag = set_attribute(img_tag, "src", f"../images/{image_file}")
            if re.search(r'alt="[^"]*"', updated_tag, re.IGNORECASE):
                return updated_tag
            return insert_attribute(updated_tag, "alt", "Chapter quote artwork")

        updated_section, img_count = img_pattern.subn(img_replacer, section_html, count=1)
        if img_count == 0:
            print(f"⚠️  No image found inside quote page for {current_file.name}; skipping image update.")
            return section_html
        return updated_section

    updated_content, replacements = section_pattern.subn(lambda m: section_replacer(m), content, count=1)
    if replacements == 0:
        print(f"⚠️  Quote page not found in {current_file.name}; no changes applied to closing art.")
    return updated_content


def fix_chapter_file(filepath: Path, image_file: str) -> None:
    print(f"Processing {filepath}…")
    original_content = filepath.read_text(encoding="utf-8")
    updated_content = original_content

    if "</head>" in updated_content:
        updated_content = add_page_break_styles(updated_content)

    updated_content = add_page_break_after_endnotes(updated_content)
    updated_content = ensure_section_attributes(
        updated_content,
        "quiz-container",
        ["chap-quiz", "avoid-break", "page-break-before"],
        {"role": "region", "aria-labelledby": "quiz-title"},
    )
    updated_content = ensure_section_attributes(
        updated_content,
        "worksheet",
        ["avoid-break", "page-break-before"],
        {"role": "region", "aria-labelledby": "ws-title"},
    )
    updated_content = update_quote_image(updated_content, image_file, filepath)

    original_tokens = extract_tokens(original_content)
    updated_tokens = extract_tokens(updated_content)

    if original_tokens != updated_tokens:
        print(f"❌  Text drift detected in {filepath.name}; reverting changes.")
        return

    if updated_content != original_content:
        filepath.write_text(updated_content, encoding="utf-8")
        print(f"✅  Updated structural markup for {filepath.name}")
    else:
        print(f"ℹ️  No structural changes required for {filepath.name}")


def main() -> None:
    output_dir = Path("output")
    for chapter_file, image_file in CHAPTERS:
        filepath = output_dir / chapter_file
        if filepath.exists():
            fix_chapter_file(filepath, image_file)
        else:
            print(f"⚠️  File not found: {filepath}")
    print("🎉  Chapter alignment complete.")


if __name__ == "__main__":
    main()
