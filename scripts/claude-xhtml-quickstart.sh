#!/bin/bash

# Claude XHTML Production - Quick Start Script
# Use this to immediately begin production-ready XHTML creation

echo "🚀 Claude XHTML Production - Quick Start"
echo "========================================="
echo ""

# Phase 1: Setup
echo "📁 Setting up production directories..."
mkdir -p output/OEBPS/text
mkdir -p output/OEBPS/styles
mkdir -p output/OEBPS/images
mkdir -p reports

echo "✅ Directories created"
echo ""

# Phase 2: List all files for Claude processing
echo "📋 File inventory for Claude production:"
echo ""
echo "FRONTMATTER FILES (7 - Single-page layouts):"
echo "  1-TitlePage.xhtml"
echo "  2-Copyright.xhtml"
echo "  3-TableOfContents.xhtml"
echo "  4-Dedication.xhtml"
echo "  5-SelfAssessment.xhtml"
echo "  6-affirmation-odyssey.xhtml"
echo "  7-Preface.xhtml"
echo ""
echo "PART DIVIDERS (4 files):"
echo "  8-Part-I-Foundations-of-Creative-Hairstyling.xhtml"
echo "  12-Part-II-Building-Your-Professional-Practice.xhtml"
echo "  18-Part-III-Advanced-Business-Strategies.xhtml"
echo "  24-Part-IV-Future-Focused-Growth.xhtml"
echo ""
echo "CHAPTER FILES (16 - 6-section structure with page breaks):"
echo "  9-chapter-i-unveiling-your-creative-odyssey.xhtml"
echo "  10-chapter-ii-refining-your-creative-toolkit.xhtml"
echo "  11-chapter-iii-reigniting-your-creative-fire.xhtml"
echo "  13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml"
echo "  14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml"
echo "  15-chapter-vi-mastering-the-business-of-hairstyling.xhtml"
echo "  16-chapter-vii-embracing-wellness-and-self-care.xhtml"
echo "  17-chapter-viii-advancing-skills-through-continuous-education.xhtml"
echo "  19-chapter-ix-stepping-into-leadership.xhtml"
echo "  20-chapter-x-crafting-enduring-legacies.xhtml"
echo "  21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml"
echo "  22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml"
echo "  23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml"
echo "  25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml"
echo "  26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml"
echo "  27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml"
echo ""
echo "BACKMATTER FILES (17 - Journal/worksheet layouts):"
echo "  28-Conclusion.xhtml through 44-bibliography.xhtml"
echo ""

# Phase 3: Claude commands
echo "🤖 READY FOR CLAUDE COMMANDS:"
echo ""
echo "1. BATCH FILE REVIEW:"
echo "   'Review all 45 XHTML files for production readiness'"
echo ""
echo "2. AUTOMATED PROCESSING:"
echo "   'node scripts/claude-xhtml-production.js'"
echo ""
echo "3. DRY RUN FIRST:"
echo "   'node scripts/claude-xhtml-production.js --dry-run --verbose'"
echo ""
echo "4. VALIDATION ONLY:"
echo "   'node scripts/claude-xhtml-production.js --validate-only'"
echo ""
echo "5. SPECIFIC CATEGORIES:"
echo "   'node scripts/claude-xhtml-production.js --frontmatter-only'"
echo "   'node scripts/claude-xhtml-production.js --chapters-only'"
echo "   'node scripts/claude-xhtml-production.js --backmatter-only'"
echo ""

# Phase 4: Node.js availability check
echo "🔧 Checking system requirements..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo "✅ Node.js is available: $NODE_VERSION"
else
    echo "⚠️  Node.js not found - install for automated processing"
fi

if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    echo "✅ npm is available: $NPM_VERSION"
else
    echo "⚠️  npm not found"
fi

echo ""

# Phase 5: Check for XHTML files
echo "📊 Checking XHTML file status..."
XHTML_COUNT=$(find OEBPS/text -name "*.xhtml" 2>/dev/null | wc -l)
OUTPUT_COUNT=$(find output/OEBPS/text -name "*.xhtml" 2>/dev/null | wc -l)

echo "  Root location (OEBPS/text): $XHTML_COUNT files"
echo "  Output location (output/OEBPS/text): $OUTPUT_COUNT files"
echo ""

# Phase 6: Ready state
echo "✨ READY TO USE CLAUDE FEATURES:"
echo ""
echo "   📝 File Reading: Use Claude Read tool"
echo "      'Read OEBPS/text/1-TitlePage.xhtml'"
echo ""
echo "   ✍️  File Writing: Use Claude Write tool"
echo "      'Write updated content to output/OEBPS/text/[filename]'"
echo ""
echo "   🔧 Code Execution: Use Claude Bash tool"
echo "      'npm run validate:xhtml'"
echo ""
echo "   ⚙️  Automation: Run production script"
echo "      'node scripts/claude-xhtml-production.js'"
echo ""

# Phase 7: Documentation references
echo "📚 DOCUMENTATION:"
echo "   Complete workflow: /root/repo/CLAUDE_XHTML_WORKFLOW.md"
echo "   Production script: /root/repo/scripts/claude-xhtml-production.js"
echo "   SDD/TDD prompts:   /root/repo/.specify/DETAILED_TASK_PROMPTS.md"
echo "   Post-completion:   /root/repo/.specify/POST_COMPLETION_GUIDE.md"
echo ""

# Phase 8: Constitutional framework
echo "📜 CONSTITUTIONAL FRAMEWORK:"
echo "   Article I:  Layout-First Principle"
echo "               - Frontmatter: min-height 100vh, single-page"
echo "               - Chapters: 6-section structure with forced page breaks"
echo ""
echo "   Article II: CLI Interface Mandate"
echo "               - All operations via npm scripts"
echo ""
echo "   Article III: Test-First Imperative"
echo "               - TDD methodology, Red-Green-Refactor"
echo ""

# Phase 9: Next steps
echo "🎯 RECOMMENDED WORKFLOW:"
echo ""
echo "   Step 1: Backup existing files"
echo "           'npm run backup:xhtml'"
echo ""
echo "   Step 2: Run dry-run to preview"
echo "           'node scripts/claude-xhtml-production.js --dry-run --verbose'"
echo ""
echo "   Step 3: Process files"
echo "           'node scripts/claude-xhtml-production.js'"
echo ""
echo "   Step 4: Validate everything"
echo "           'npm run validate:xhtml'"
echo "           'npm run validate:assets'"
echo "           'npm run validate:toc'"
echo ""
echo "   Step 5: Build production EPUB"
echo "           'npm run build:production'"
echo ""
echo "   Step 6: Final validation"
echo "           './validate-epub.sh'"
echo ""

echo "═══════════════════════════════════════════════════════════"
echo "Ready to begin! Start with Step 1 above."
echo "═══════════════════════════════════════════════════════════"
echo ""

# Make this script executable
chmod +x "$0"
