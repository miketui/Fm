import os
import re
from pathlib import Path

# Configuration
XHTML_DIR = Path('REBRANDED_OUTPUT/xhtml')
CHAPTER_FILES = [
    '9-chapter-i-unveiling-your-creative-odyssey.xhtml',
    '10-chapter-ii-refining-your-creative-toolkit.xhtml',
    '11-chapter-iii-reigniting-your-creative-fire.xhtml',
    '13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml',
    '14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml',
    '15-chapter-vi-mastering-the-business-of-hairstyling.xhtml',
    '16-chapter-vii-embracing-wellness-and-self-care.xhtml',
    '17-chapter-viii-advancing-skills-through-continuous-education.xhtml',
    '19-chapter-ix-stepping-into-leadership.xhtml',
    '20-chapter-x-crafting-enduring-legacies.xhtml',
    '21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml',
    '22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml',
    '23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml',
    '25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml',
    '26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml',
    '27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml'
]

def analyze_and_fix():
    print("Analyzing and fixing chapters...")
    for filename in CHAPTER_FILES:
        filepath = XHTML_DIR / filename
        if not filepath.exists():
            print(f"❌ File not found: {filename}")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        fixed = False
        log_msgs = []

        # 1. Remove duplicate quote sections
        # Pattern: look for multiple image-quote sections or quote-page sections
        # We want to keep the LAST one or merge them. The instructions say "Delete the second one entirely, keeping only the first."
        # Wait, instructions: "If you find TWO... Delete the second one entirely, keeping only the first."
        # But wait, usually the last one is the one at the end of the file.
        # Let's see where they are.
        
        # Regex to find quote sections
        # Matches <section class="...quote..."> ... </section>
        # We need to be careful with regex on HTML.
        
        # Strategy:
        # Find the worksheet end: </section>  <!-- This is where the worksheet ends --> or similar.
        # The instructions say: locate </section>  <!-- End worksheet --> (or similar)
        # Then everything after that is the target area.
        
        # Let's find the worksheet end marker. It varies slightly in actual files?
        # In the file I read: </section>\n\n<!-- PAGE BREAK --> ... <!-- SECTION 5: WORKSHEET ... --> ... </section>
        
        # It seems safer to identify the "Quote Image" section(s) specifically by content (e.g. img src="...-quote.jpeg")
        
        quote_img_pattern = re.compile(r'<section[^>]*class="[^"]*quote[^"]*"[^>]*>.*?<img[^>]*src="[^"]*-quote\.jpeg"[^>]*>.*?</figure>\s*</section>', re.DOTALL | re.IGNORECASE)
        
        matches = list(quote_img_pattern.finditer(content))
        
        if len(matches) > 1:
            log_msgs.append(f"Found {len(matches)} quote sections. Removing extras.")
            # Keep the FIRST one as per instructions, but wait, usually we want the one at the very end.
            # Instructions: "If you find TWO quote image sections... Delete the second one entirely, keeping only the first."
            # The example shows the first one being correct-ish (or the target to fix) and the second one being a "duplicate".
            # I will remove all but the first match found in the text.
            
            # Reconstruct content:
            # Everything before 2nd match + everything after 2nd match... 
            # Actually, let's just keep the first one.
            
            # We need to process from last to first to not mess up indices, but we want to keep the FIRST match.
            # So remove matches[1], matches[2]...
            
            for m in reversed(matches[1:]):
                start, end = m.span()
                content = content[:start] + content[end:]
            
            fixed = True

        # 2. Fix the remaining quote section (class and page break)
        # Find the single remaining quote section
        match = quote_img_pattern.search(content)
        if match:
            quote_section = match.group(0)
            start, end = match.span()
            
            # Check for page break before it
            # Look at text immediately preceding 'start'
            preceding_text = content[max(0, start-200):start]
            
            has_page_break = '<div class="page-break"></div>' in preceding_text
            
            new_quote_section = quote_section
            
            # Fix class
            if 'quote-page page-break-before' not in new_quote_section:
                # Replace class="..." with class="quote-page page-break-before"
                # Or simplistic replacement
                new_quote_section = re.sub(r'class="[^"]*quote[^"]*"', 'class="quote-page page-break-before"', new_quote_section, flags=re.IGNORECASE)
                if 'role="complementary"' not in new_quote_section:
                     new_quote_section = new_quote_section.replace('<section', '<section role="complementary"')
                log_msgs.append("Fixed section class.")
                fixed = True

            # Ensure page break
            if not has_page_break:
                # Insert page break before the section
                # We replace the section with "\n<!-- PAGE BREAK -->\n<div class=\"page-break\"></div>\n\n" + new_section
                replacement = '\n<!-- PAGE BREAK -->\n<div class="page-break"></div>\n\n' + new_quote_section
                content = content[:start] + replacement + content[end:]
                log_msgs.append("Added missing page break.")
                fixed = True
            elif new_quote_section != quote_section:
                 # Just replace the section if only class changed
                 content = content[:start] + new_quote_section + content[end:]
                 fixed = True

        else:
            log_msgs.append("⚠️ No quote section found!")

        if fixed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed {filename}: {', '.join(log_msgs)}")
        else:
            print(f"👍 {filename} is already correct.")

if __name__ == '__main__':
    analyze_and_fix()
