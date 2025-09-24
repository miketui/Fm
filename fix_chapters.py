#!/usr/bin/env python3
"""
Script to fix chapter formatting:
1. Add page breaks after endnotes
2. Format quizzes with exactly 4 multiple choice questions (A-D) on single page
3. Format worksheets to fit on one page after quiz
4. Add centered quote images as final page of each chapter
5. Add forced page breaks between sections
"""

import re
import os
from pathlib import Path

# Chapter files and their corresponding quote images
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

def add_page_break_styles(content):
    """Add CSS for page breaks"""
    style_section = """
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

    # Insert styles before closing head tag
    return content.replace('</head>', f'{style_section}</head>')

def fix_quiz_section(content):
    """Ensure quiz has exactly 4 multiple choice questions A-D on one page"""
    # Pattern to find quiz section
    quiz_pattern = r'(<section class="quiz-container[^"]*"[^>]*>.*?</section>)'

    def replace_quiz(match):
        quiz_section = match.group(1)

        # Extract quiz questions - look for question patterns
        questions = re.findall(r'<p[^>]*class="quiz-question"[^>]*>(.*?)</p>', quiz_section, re.DOTALL)

        if not questions:
            # Fallback - look for numbered questions
            questions = re.findall(r'<p[^>]*>(\d+\.\s*.*?)</p>', quiz_section, re.DOTALL)

        # Create standardized 4-question quiz
        if len(questions) >= 4:
            # Use existing questions
            quiz_questions = questions[:4]
        else:
            # Create default questions if not enough exist
            quiz_questions = [
                "1. What is the primary focus of this chapter's main concept?",
                "2. Which technique or approach was highlighted as most effective?",
                "3. What should be prioritized when applying these principles?",
                "4. How does this chapter's content connect to professional development?"
            ]

        # Build new quiz section
        new_quiz = f'''<section class="quiz-container chap-quiz avoid-break page-break-before" role="region" aria-labelledby="quiz-title">
<h2 id="quiz-title" class="quiz-title">Chapter Quiz</h2>

<div class="quiz-question-block">
<p class="quiz-question"><strong>{quiz_questions[0]}</strong></p>
<ul class="quiz-options">
<li class="quiz-option"><span class="opt-label">A)</span> Focus on technical precision and speed</li>
<li class="quiz-option"><span class="opt-label">B)</span> Emphasize client consultation and communication</li>
<li class="quiz-option"><span class="opt-label">C)</span> Prioritize the most expensive products and tools</li>
<li class="quiz-option"><span class="opt-label">D)</span> Follow traditional methods without adaptation</li>
</ul>
</div>

<div class="quiz-question-block">
<p class="quiz-question"><strong>{quiz_questions[1] if len(quiz_questions) > 1 else "2. Which approach demonstrates professional excellence?"}</strong></p>
<ul class="quiz-options">
<li class="quiz-option"><span class="opt-label">A)</span> Continuing education and skill development</li>
<li class="quiz-option"><span class="opt-label">B)</span> Working in isolation without feedback</li>
<li class="quiz-option"><span class="opt-label">C)</span> Focusing only on popular trends</li>
<li class="quiz-option"><span class="opt-label">D)</span> Avoiding challenging or diverse clientele</li>
</ul>
</div>

<div class="quiz-question-block">
<p class="quiz-question"><strong>{quiz_questions[2] if len(quiz_questions) > 2 else "3. What is essential for building a successful hairstyling practice?"}</strong></p>
<ul class="quiz-options">
<li class="quiz-option"><span class="opt-label">A)</span> Client relationships and trust-building</li>
<li class="quiz-option"><span class="opt-label">B)</span> Working as quickly as possible</li>
<li class="quiz-option"><span class="opt-label">C)</span> Using identical techniques for all clients</li>
<li class="quiz-option"><span class="opt-label">D)</span> Avoiding feedback or self-reflection</li>
</ul>
</div>

<div class="quiz-question-block">
<p class="quiz-question"><strong>{quiz_questions[3] if len(quiz_questions) > 3 else "4. How does this chapter contribute to professional growth?"}</strong></p>
<ul class="quiz-options">
<li class="quiz-option"><span class="opt-label">A)</span> Provides actionable steps for development</li>
<li class="quiz-option"><span class="opt-label">B)</span> Guarantees immediate financial success</li>
<li class="quiz-option"><span class="opt-label">C)</span> Replaces the need for formal training</li>
<li class="quiz-option"><span class="opt-label">D)</span> Focuses only on theoretical knowledge</li>
</ul>
</div>
</section>'''

        return new_quiz

    return re.sub(quiz_pattern, replace_quiz, content, flags=re.DOTALL)

def fix_worksheet_section(content):
    """Ensure worksheet fits on one page after quiz"""
    # Pattern to find worksheet section
    worksheet_pattern = r'(<section class="worksheet[^"]*"[^>]*>.*?</section>)'

    def replace_worksheet(match):
        worksheet_section = match.group(1)

        # Create standardized worksheet that fits on one page
        new_worksheet = '''<section class="worksheet avoid-break page-break-before" role="region" aria-labelledby="ws-title">
<h2 id="ws-title" class="worksheet-title">Chapter Worksheet</h2>
<div class="worksheet-content">
<p><strong>Reflection Questions:</strong></p>
<ol>
<li><strong>What is the most important concept you learned from this chapter?</strong></li>
<p>_____________________________________________________________________</p>
<p>_____________________________________________________________________</p>
<p>_____________________________________________________________________</p>

<li><strong>How will you apply this knowledge in your professional practice?</strong></li>
<p>_____________________________________________________________________</p>
<p>_____________________________________________________________________</p>
<p>_____________________________________________________________________</p>

<li><strong>What specific action will you take this week to implement these ideas?</strong></li>
<p>_____________________________________________________________________</p>
<p>_____________________________________________________________________</p>
<p>_____________________________________________________________________</p>

<li><strong>How does this chapter's content connect to your professional goals?</strong></li>
<p>_____________________________________________________________________</p>
<p>_____________________________________________________________________</p>
<p>_____________________________________________________________________</p>
</ol>
</div>
</section>'''

        return new_worksheet

    return re.sub(worksheet_pattern, replace_worksheet, content, flags=re.DOTALL)

def add_page_break_after_endnotes(content):
    """Add page break after endnotes section"""
    # Find endnotes section and add page break class
    endnotes_pattern = r'(<aside class="endnotes"[^>]*>.*?</aside>)'

    def replace_endnotes(match):
        endnotes_section = match.group(1)
        # Add page-break-after class
        modified_section = endnotes_section.replace('class="endnotes"', 'class="endnotes page-break-after"')
        return modified_section

    return re.sub(endnotes_pattern, replace_endnotes, content, flags=re.DOTALL)

def add_quote_image_page(content, image_file):
    """Add centered quote image as final page"""
    # Remove existing closing section with image
    content = re.sub(r'<section class="closing"[^>]*>.*?</section>', '', content, flags=re.DOTALL)

    # Add new quote page before closing tags
    quote_page = f'''
<section class="quote-page">
<figure>
<img src="../images/{image_file}" alt="Inspirational quote for this chapter" />
</figure>
</section>'''

    # Insert before closing main/body tags
    content = content.replace('</main>', f'{quote_page}</main>')

    return content

def fix_chapter_file(filepath, image_file):
    """Fix a single chapter file"""
    print(f"Fixing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply all fixes
    content = add_page_break_styles(content)
    content = add_page_break_after_endnotes(content)
    content = fix_quiz_section(content)
    content = fix_worksheet_section(content)
    content = add_quote_image_page(content, image_file)

    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Fixed {filepath}")

def main():
    """Fix all chapter files"""
    output_dir = Path("output")

    for chapter_file, image_file in CHAPTERS:
        filepath = output_dir / chapter_file
        if filepath.exists():
            fix_chapter_file(filepath, image_file)
        else:
            print(f"⚠️  File not found: {filepath}")

    print("🎉 All chapter files have been fixed!")

if __name__ == "__main__":
    main()