#!/usr/bin/env python3
"""
Script to convert all 16 existing chapter XHTML files to the new master template format.
Preserves all original content word-for-word while applying consistent formatting.
"""

import re
from pathlib import Path

# Chapter mapping with titles
CHAPTERS = [
    {"num": "I", "roman": "I", "file": "9-chapter-i-unveiling-your-creative-odyssey.xhtml", "title_lines": ["Unveiling", "Your", "Creative", "Odyssey"]},
    {"num": "II", "roman": "II", "file": "10-chapter-ii-refining-your-creative-toolkit.xhtml", "title_lines": ["Refining", "Your", "Creative", "Toolkit"]},
    {"num": "III", "roman": "III", "file": "11-chapter-iii-reigniting-your-creative-fire.xhtml", "title_lines": ["Reigniting", "Your", "Creative", "Fire"]},
    {"num": "IV", "roman": "IV", "file": "13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml", "title_lines": ["The", "Art", "of", "Networking", "in", "Freelance", "Hairstyling"]},
    {"num": "V", "roman": "V", "file": "14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml", "title_lines": ["Cultivating", "Creative", "Excellence", "Through", "Mentorship"]},
    {"num": "VI", "roman": "VI", "file": "15-chapter-vi-mastering-the-business-of-hairstyling.xhtml", "title_lines": ["Mastering", "the", "Business", "of", "Hairstyling"]},
    {"num": "VII", "roman": "VII", "file": "16-chapter-vii-embracing-wellness-and-self-care.xhtml", "title_lines": ["Embracing", "Wellness", "and", "Self-Care"]},
    {"num": "VIII", "roman": "VIII", "file": "17-chapter-viii-advancing-skills-through-continuous-education.xhtml", "title_lines": ["Advancing", "Skills", "Through", "Continuous", "Education"]},
    {"num": "IX", "roman": "IX", "file": "19-chapter-ix-stepping-into-leadership.xhtml", "title_lines": ["Stepping", "Into", "Leadership"]},
    {"num": "X", "roman": "X", "file": "20-chapter-x-crafting-enduring-legacies.xhtml", "title_lines": ["Crafting", "Enduring", "Legacies"]},
    {"num": "XI", "roman": "XI", "file": "21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml", "title_lines": ["Advanced", "Digital", "Strategies", "for", "Freelance", "Hairstylists"]},
    {"num": "XII", "roman": "XII", "file": "22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml", "title_lines": ["Financial", "Wisdom", "Building", "Sustainable", "Ventures"]},
    {"num": "XIII", "roman": "XIII", "file": "23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml", "title_lines": ["Embracing", "Ethics", "and", "Sustainability", "in", "Hairstyling"]},
    {"num": "XIV", "roman": "XIV", "file": "25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml", "title_lines": ["The", "Impact", "of", "AI", "on", "the", "Beauty", "Industry"]},
    {"num": "XV", "roman": "XV", "file": "26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml", "title_lines": ["Cultivating", "Resilience", "and", "Well-Being", "in", "Hairstyling"]},
    {"num": "XVI", "roman": "XVI", "file": "27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml", "title_lines": ["Tresses", "and", "Textures", "-", "Embracing", "Diversity", "in", "Hairstyling"]},
]

def extract_content(html_content):
    """Extract key content sections from original chapter HTML."""

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL)
    title = title_match.group(1) if title_match else ""

    # Extract bible quote
    quote_match = re.search(r'<blockquote class="bible-quote-text"[^>]*>(.*?)</blockquote>', html_content, re.DOTALL)
    quote = quote_match.group(1).strip() if quote_match else ""

    # Extract bible reference
    ref_match = re.search(r'<figcaption class="bible-quote-reference"[^>]*>(.*?)</figcaption>', html_content, re.DOTALL)
    reference = ref_match.group(1).strip() if ref_match else ""

    # Extract introduction section
    intro_match = re.search(r'<div class="introduction-paragraph[^"]*">(.*?)</div>', html_content, re.DOTALL)
    introduction = intro_match.group(1).strip() if intro_match else ""

    # Extract main body content
    body_match = re.search(r'<section class="chap-body"[^>]*>.*?<div class="content-area">(.*?)</div>\s*</section>', html_content, re.DOTALL)
    body_content = body_match.group(1).strip() if body_match else ""

    # Extract endnotes
    endnotes_match = re.search(r'<aside class="endnotes[^"]*"[^>]*>(.*?)</aside>', html_content, re.DOTALL)
    endnotes = endnotes_match.group(1).strip() if endnotes_match else ""

    # Extract quiz section
    quiz_match = re.search(r'<section class="quiz-container[^"]*"[^>]*>(.*?)</section>', html_content, re.DOTALL)
    quiz = quiz_match.group(1).strip() if quiz_match else ""

    # Extract worksheet section
    worksheet_match = re.search(r'<section class="worksheet[^"]*"[^>]*>(.*?)</section>', html_content, re.DOTALL)
    worksheet = worksheet_match.group(1).strip() if worksheet_match else ""

    return {
        'title': title,
        'quote': quote,
        'reference': reference,
        'introduction': introduction,
        'body': body_content,
        'endnotes': endnotes,
        'quiz': quiz,
        'worksheet': worksheet
    }

def create_chapter_xhtml(chapter_info, content):
    """Generate complete chapter XHTML using master template format."""

    roman = chapter_info['roman']
    title_lines = '\n'.join([f'          <div class="title-line">{line}</div>' for line in chapter_info['title_lines']])
    quote_img = f"chapter-{roman.lower()}-quote.jpeg"

    xhtml = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
  <head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{content['title']}</title>
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/print.css" media="print"/>
</head>
  <body class="chapter-page">
    <main role="main" epub:type="bodymatter chapter">
    <section class="chap-title" role="region">
      <figure class="chapter-number-figure" role="group" aria-label="Chapter number {roman}">
        <img class="chapter-number-brush" src="../images/brushstroke.svg" alt="Decorative teal brushstroke background" />
        <figcaption class="chapter-number-roman">{roman}</figcaption>
      </figure>

      <div class="title-stack">
        <div class="title-bar"></div>
        <div class="title-lines">
{title_lines}
        </div>
      </div>
      <figure class="bible-quote-container image-quote" role="group" aria-labelledby="bq-text bq-ref">
        <blockquote class="bible-quote-text" id="bq-text">
          {content['quote']}
        </blockquote>
        <figcaption class="bible-quote-reference" id="bq-ref">{content['reference']}</figcaption>
      </figure>
      <h2 class="introduction-heading">Introduction</h2>
      <div class="introduction-paragraph dropcap-first-letter">
        {content['introduction']}
      </div>
    </section>

<!-- PAGE BREAK -->
<div class="page-break"></div>

<!-- PAGES 2-4: BODY CONTENT -->
<section class="chap-body" role="region">
      <div class="content-area">
{content['body']}
      </div>
      <aside class="endnotes page-break-after" role="complementary">
  {content['endnotes']}
</aside>

<!-- PAGE BREAK -->
<div class="page-break"></div>

<!-- PAGE 6: QUIZ & WORKSHEET -->
<section class="quiz-container chap-quiz avoid-break page-break-before" role="region" aria-labelledby="quiz-title">
{content['quiz']}
</section>
      <section class="worksheet avoid-break page-break-before" role="region" aria-labelledby="ws-title">
{content['worksheet']}
</section>


    </section>

<section class="quote-page">
<figure>
<img src="../images/{quote_img}" alt="Inspirational quote for this chapter" />
</figure>
</section></main>
  </body>
</html>
'''

    return xhtml

def main():
    """Process all 16 chapters."""

    source_dir = Path('/root/repo/OEBPS/text')
    output_dir = Path('/root/repo/REBRANDED_OUTPUT/xhtml')
    output_dir.mkdir(exist_ok=True)

    for chapter in CHAPTERS:
        print(f"Processing Chapter {chapter['roman']}...")

        # Read original chapter
        source_file = source_dir / chapter['file']
        with open(source_file, 'r', encoding='utf-8') as f:
            original_html = f.read()

        # Extract content
        content = extract_content(original_html)

        # Generate new formatted chapter
        new_html = create_chapter_xhtml(chapter, content)

        # Write to output
        output_file = output_dir / chapter['file']
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(new_html)

        print(f"  ✓ Created {output_file.name}")

    print(f"\n✅ All 16 chapters created successfully in {output_dir}")

if __name__ == '__main__':
    main()
