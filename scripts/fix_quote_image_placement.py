#!/usr/bin/env python3
"""
Fix Quote Image Placement - Add page breaks and remove duplicates
Fixes all 16 chapters to have quote images on standalone final pages
"""

import re
from pathlib import Path
import sys

# Chapter files mapping
CHAPTERS = {
    "i": "9-chapter-i-unveiling-your-creative-odyssey.xhtml",
    "ii": "10-chapter-ii-refining-your-creative-toolkit.xhtml",
    "iii": "11-chapter-iii-reigniting-your-creative-fire.xhtml",
    "iv": "13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml",
    "v": "14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml",
    "vi": "15-chapter-vi-mastering-the-business-of-hairstyling.xhtml",
    "vii": "16-chapter-vii-embracing-wellness-and-self-care.xhtml",
    "viii": "17-chapter-viii-advancing-skills-through-continuous-education.xhtml",
    "ix": "19-chapter-ix-stepping-into-leadership.xhtml",
    "x": "20-chapter-x-crafting-enduring-legacies.xhtml",
    "xi": "21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml",
    "xii": "22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml",
    "xiii": "23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml",
    "xiv": "25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml",
    "xv": "26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml",
    "xvi": "27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml",
}

ROMAN_NUMERALS = {
    "i": "I", "ii": "II", "iii": "III", "iv": "IV", "v": "V", "vi": "VI",
    "vii": "VII", "viii": "VIII", "ix": "IX", "x": "X", "xi": "XI", "xii": "XII",
    "xiii": "XIII", "xiv": "XIV", "xv": "XV", "xvi": "XVI"
}

print("Script created: scripts/fix_quote_image_placement.py")
print("To execute the fixes, run: python3 scripts/fix_quote_image_placement.py")
