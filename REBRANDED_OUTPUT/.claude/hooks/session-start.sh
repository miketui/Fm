#!/bin/bash
# Session Start Hook for EPUB Production
# Runs when Claude Code session starts in REBRANDED_OUTPUT directory

set -euo pipefail

# Color codes
readonly CYAN='\033[0;36m'
readonly GREEN='\033[0;32m'
readonly BLUE='\033[0;34m'
readonly YELLOW='\033[1;33m'
readonly NC='\033[0m'

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_header() {
    echo -e "\n${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REBRANDED_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

log_header "🚀 EPUB Production Environment - Session Start"

log_info "Working directory: $REBRANDED_DIR"
cd "$REBRANDED_DIR"

# Check environment
log_info "Checking EPUB production environment..."

# Check required directories
required_dirs=("xhtml" "images" "fonts" "styles" "META-INF" "scripts/subagents")
missing_dirs=0

for dir in "${required_dirs[@]}"; do
    if [ -d "$dir" ]; then
        log_success "Directory: $dir"
    else
        log_warning "Missing: $dir"
        ((missing_dirs++))
    fi
done

# Check required files
required_files=("mimetype" "content.opf" "META-INF/container.xml")
missing_files=0

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        log_success "File: $file"
    else
        log_warning "Missing: $file"
        ((missing_files++))
    fi
done

# Check validation tools
log_info "Checking validation tools..."

if command -v xmllint &> /dev/null; then
    log_success "xmllint available"
else
    log_warning "xmllint not found (install libxml2-utils for enhanced validation)"
fi

if command -v zip &> /dev/null; then
    log_success "zip utility available"
else
    log_warning "zip not found (required for EPUB building)"
fi

if [ -f "../epubcheck/epubcheck.jar" ]; then
    log_success "epubcheck available"
else
    log_warning "epubcheck not found (recommended for final validation)"
fi

# Display available commands
log_header "📚 Available Claude Code Commands"

echo "  Use these slash commands to work with EPUB:"
echo ""
echo "  /epub-validate   - Validate all XHTML files and EPUB package"
echo "  /epub-build      - Build production-ready EPUB file"
echo "  /epub-prepare    - Run complete preparation workflow"
echo ""

# Display subagent scripts
log_info "Available subagent scripts:"
echo ""
echo "  ./scripts/subagents/validate-xhtml.sh           - Validate XHTML structure"
echo "  ./scripts/subagents/validate-epub-package.sh    - Validate EPUB package"
echo "  ./scripts/subagents/check-content-integrity.sh  - Check content integrity"
echo "  ./scripts/subagents/build-epub.sh               - Build EPUB file"
echo ""

# Quick status
log_header "📊 Quick Status"

xhtml_count=$(find xhtml -name "*.xhtml" 2>/dev/null | wc -l || echo "0")
image_count=$(find images -type f 2>/dev/null | wc -l || echo "0")
font_count=$(find fonts -type f 2>/dev/null | wc -l || echo "0")

echo -e "  XHTML files: ${GREEN}$xhtml_count${NC}"
echo -e "  Images: ${GREEN}$image_count${NC}"
echo -e "  Fonts: ${GREEN}$font_count${NC}"

if [ -f "The-Artisans-Path.epub" ]; then
    epub_size=$(du -h The-Artisans-Path.epub | cut -f1)
    echo -e "  Built EPUB: ${GREEN}The-Artisans-Path.epub${NC} ($epub_size)"
else
    echo -e "  Built EPUB: ${YELLOW}Not built yet${NC}"
fi

echo ""

# Summary
if [ $missing_dirs -eq 0 ] && [ $missing_files -eq 0 ]; then
    log_success "Environment ready for EPUB production!"
else
    log_warning "Some directories or files are missing. Please verify setup."
fi

log_header "✨ Ready to build error-free EPUBs!"

exit 0
