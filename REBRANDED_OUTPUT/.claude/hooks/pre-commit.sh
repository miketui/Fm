#!/bin/bash
# Pre-Commit Hook for EPUB XHTML Validation
# Validates XHTML files before allowing commits to ensure quality

set -euo pipefail

# Color codes
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly CYAN='\033[0;36m'
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

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

log_header() {
    echo -e "\n${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REBRANDED_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

log_header "🔍 Pre-Commit XHTML Validation"

cd "$REBRANDED_DIR"

# Get list of staged XHTML files
staged_xhtml_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.xhtml$' || true)

if [ -z "$staged_xhtml_files" ]; then
    log_info "No XHTML files staged for commit. Skipping validation."
    exit 0
fi

log_info "Validating staged XHTML files..."
echo ""

errors=0
warnings=0
files_checked=0

# Validate each staged XHTML file
while IFS= read -r file; do
    if [ ! -f "$file" ]; then
        continue
    fi

    ((files_checked++))
    filename=$(basename "$file")

    echo -e "${CYAN}Checking: $filename${NC}"

    # XML well-formedness check
    if command -v xmllint &> /dev/null; then
        if xmllint --noout "$file" 2>/dev/null; then
            log_success "XML structure valid"
        else
            log_error "XML syntax error in $filename"
            xmllint --noout "$file" 2>&1 | head -3
            ((errors++))
        fi
    else
        # Basic check without xmllint
        if grep -q "^<?xml" "$file" && grep -q "</html>" "$file"; then
            log_success "Basic XML structure OK"
        else
            log_error "Basic XML structure check failed for $filename"
            ((errors++))
        fi
    fi

    # DOCTYPE check
    if ! grep -q '<!DOCTYPE html' "$file"; then
        log_warning "Missing DOCTYPE in $filename"
        ((warnings++))
    fi

    # XHTML namespace check
    if ! grep -q 'xmlns="http://www.w3.org/1999/xhtml"' "$file"; then
        log_warning "Missing XHTML namespace in $filename"
        ((warnings++))
    fi

    # Check for unclosed tags (basic)
    if grep -qE '<img[^>]*[^/]>' "$file" 2>/dev/null; then
        log_warning "Potentially unclosed img tags in $filename"
        ((warnings++))
    fi

    if grep -qE '<br[^/]>' "$file" 2>/dev/null; then
        log_warning "Unclosed br tags in $filename (should be <br/>)"
        ((warnings++))
    fi

    # Check for images without alt attributes
    if grep -q '<img' "$file" 2>/dev/null; then
        if grep '<img' "$file" | grep -v 'alt=' >/dev/null 2>&1; then
            log_warning "Images without alt attributes in $filename"
            ((warnings++))
        fi
    fi

    echo ""

done <<< "$staged_xhtml_files"

# Summary
log_header "Validation Summary"

echo -e "Files checked: ${CYAN}$files_checked${NC}"
echo -e "Errors: ${RED}$errors${NC}"
echo -e "Warnings: ${YELLOW}$warnings${NC}"
echo ""

# Decide whether to allow commit
if [ $errors -gt 0 ]; then
    log_header "❌ Commit blocked due to validation errors"
    echo ""
    echo "Please fix the errors in your XHTML files before committing."
    echo ""
    echo "To bypass this check (not recommended), use:"
    echo "  git commit --no-verify"
    echo ""
    exit 1
elif [ $warnings -gt 0 ]; then
    log_header "⚠️  Commit allowed with warnings"
    echo ""
    echo "Your XHTML files have warnings but no critical errors."
    echo "Consider fixing the warnings for better EPUB quality."
    echo ""
    exit 0
else
    log_header "✅ All validation checks passed!"
    echo ""
    exit 0
fi
