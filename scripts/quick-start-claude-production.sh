#!/bin/bash

# Claude XHTML Production - Quick Start Script
# Use this to immediately begin production-ready XHTML creation

echo "🚀 Claude XHTML Production - Quick Start"
echo "========================================="

# Phase 1: Setup
echo "📁 Setting up production directories..."
mkdir -p output/OEBPS/text
mkdir -p output/OEBPS/styles  
mkdir -p output/OEBPS/images
mkdir -p reports

# Phase 2: List all files for Claude processing
echo "📋 File inventory for Claude production:"
echo ""
echo "FRONTMATTER FILES (Single-page layouts):"
echo "- 1-TitlePage.xhtml"
echo "- 2-Copyright.xhtml"  
echo "- 3-TableOfContents.xhtml"
echo "- 4-Dedication.xhtml"
echo "- 5-SelfAssessment.xhtml"
echo "- 6-affirmation-odyssey.xhtml"
echo "- 7-Preface.xhtml"
echo ""
echo "CHAPTER FILES (6-section structure with page breaks):"
echo "- 9-chapter-i-unveiling-your-creative-odyssey.xhtml"
echo "- 10-chapter-ii-refining-your-creative-toolkit.xhtml"
echo "- 11-chapter-iii-reigniting-your-creative-fire.xhtml"
echo "- 13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml"
echo "- 14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml"
echo "- 15-chapter-vi-mastering-the-business-of-hairstyling.xhtml"
echo "- 16-chapter-vii-embracing-wellness-and-self-care.xhtml"
echo "- 17-chapter-viii-advancing-skills-through-continuous-education.xhtml"
echo "- 19-chapter-ix-stepping-into-leadership.xhtml"
echo "- 20-chapter-x-crafting-enduring-legacies.xhtml"
echo "- 21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml"
echo "- 22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml"
echo "- 23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml"
echo "- 25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml"
echo "- 26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml"
echo "- 27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml"
echo ""
echo "PART DIVIDERS:"
echo "- 8-Part-I-Foundations-of-Creative-Hairstyling.xhtml"
echo "- 12-Part-II-Building-Your-Professional-Practice.xhtml"
echo "- 18-Part-III-Advanced-Business-Strategies.xhtml"
echo "- 24-Part-IV-Future-Focused-Growth.xhtml"
echo ""
echo "BACKMATTER FILES (Journal/worksheet layouts):"
echo "- 28-Conclusion.xhtml through 44-bibliography.xhtml"
echo ""

# Phase 3: Claude commands
echo "🤖 READY FOR CLAUDE COMMANDS:"
echo ""
echo "1. BATCH FILE CREATION:"
echo "   Command: 'Use create_file to generate all 45 production-ready XHTML files'"
echo ""
echo "2. AUTOMATED PROCESSING:"
echo "   Command: 'node /root/repo/scripts/claude-xhtml-production.js'"
echo ""
echo "3. VALIDATION:"
echo "   Command: 'Validate all XHTML files for production readiness'"
echo ""

# Phase 4: Node.js availability check
echo "🔧 Checking Node.js availability..."
if command -v node &> /dev/null; then
    echo "✅ Node.js is available"
    node --version
else
    echo "⚠️  Node.js not found - install for automated processing"
fi

# Phase 5: Ready state
echo ""
echo "✨ READY TO USE CLAUDE FEATURES:"
echo "   - File creation: create_file tool"
echo "   - Code execution: Bash tool with Node.js scripts"  
echo "   - Validation: Automated checking and reporting"
echo ""
echo "🎯 START WITH: Ask Claude to create the first XHTML file using create_file"
echo ""
echo "📚 Full workflow guide: /root/repo/CLAUDE_XHTML_WORKFLOW.md"
echo "⚙️  Production script: /root/repo/scripts/claude-xhtml-production.js"

# Make executable
chmod +x "$0"
