#!/bin/bash
# XHTML Validation Subagent
# Validates all XHTML files for proper structure, syntax, and EPUB compliance

set -euo pipefail

# Color codes
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly CYAN='\033[0;36m'
readonly NC='\033[0m'

# Counters
total_files=0
valid_files=0
error_files=0
warning_count=0

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REBRANDED_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
    ((warning_count++))
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

log_section() {
    echo -e "\n${CYAN}═══════════════════════════════════════════${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════${NC}\n"
}

# Check if xmllint is available
check_xmllint() {
    if ! command -v xmllint &> /dev/null; then
        log_warning "xmllint not found. Install libxml2-utils for detailed validation."
        return 1
    fi
    return 0
}

# Validate XML well-formedness
validate_xml_structure() {
    local file="$1"
    local filename=$(basename "$file")

    if command -v xmllint &> /dev/null; then
        if xmllint --noout "$file" 2>/dev/null; then
            return 0
        else
            log_error "XML syntax error in $filename"
            xmllint --noout "$file" 2>&1 | head -5
            return 1
        fi
    else
        # Basic validation without xmllint
        if grep -q "^<?xml" "$file" && grep -q "</html>" "$file"; then
            return 0
        else
            log_error "Basic XML structure check failed for $filename"
            return 1
        fi
    fi
}

# Check XHTML DOCTYPE
check_doctype() {
    local file="$1"
    local filename=$(basename "$file")

    if ! grep -q '<!DOCTYPE html' "$file"; then
        log_warning "Missing or incorrect DOCTYPE in $filename"
        return 1
    fi
    return 0
}

# Check HTML namespace
check_html_namespace() {
    local file="$1"
    local filename=$(basename "$file")

    if ! grep -q 'xmlns="http://www.w3.org/1999/xhtml"' "$file"; then
        log_warning "Missing XHTML namespace in $filename"
        return 1
    fi
    return 0
}

# Check EPUB namespace (if epub:type is used)
check_epub_namespace() {
    local file="$1"
    local filename=$(basename "$file")

    if grep -q 'epub:type=' "$file"; then
        if ! grep -q 'xmlns:epub="http://www.idpf.org/2007/ops"' "$file"; then
            log_warning "epub:type used but EPUB namespace missing in $filename"
            return 1
        fi
    fi
    return 0
}

# Check for common XHTML issues
check_common_issues() {
    local file="$1"
    local filename=$(basename "$file")
    local issues=0

    # Check for unclosed img tags
    if grep -q '<img[^>]*[^/]>' "$file" 2>/dev/null; then
        log_warning "Potentially unclosed img tags in $filename"
        ((issues++))
    fi

    # Check for unclosed br tags
    if grep -q '<br[^/]>' "$file" 2>/dev/null; then
        log_warning "Unclosed br tags in $filename (should be <br/>)"
        ((issues++))
    fi

    # Check for unclosed hr tags
    if grep -q '<hr[^/]>' "$file" 2>/dev/null; then
        log_warning "Unclosed hr tags in $filename (should be <hr/>)"
        ((issues++))
    fi

    # Check for missing alt attributes on images
    if grep -q '<img' "$file" 2>/dev/null; then
        local img_lines=$(grep '<img' "$file" | grep -v 'alt=' || true)
        if [ -n "$img_lines" ]; then
            log_warning "Images without alt attributes in $filename"
            ((issues++))
        fi
    fi

    return $issues
}

# Check character encoding
check_encoding() {
    local file="$1"
    local filename=$(basename "$file")

    if ! grep -q 'charset="utf-8"' "$file" && ! grep -q "charset='utf-8'" "$file"; then
        log_warning "UTF-8 charset declaration missing or incorrect in $filename"
        return 1
    fi
    return 0
}

# Validate single XHTML file
validate_xhtml_file() {
    local file="$1"
    local filename=$(basename "$file")
    local file_errors=0

    echo -e "${CYAN}Validating: $filename${NC}"

    ((total_files++))

    # XML well-formedness check
    if ! validate_xml_structure "$file"; then
        ((error_files++))
        ((file_errors++))
    fi

    # DOCTYPE check
    check_doctype "$file" || ((file_errors++))

    # Namespace checks
    check_html_namespace "$file" || ((file_errors++))
    check_epub_namespace "$file" || ((file_errors++))

    # Encoding check
    check_encoding "$file" || ((file_errors++))

    # Common issues check
    check_common_issues "$file" || ((file_errors++))

    if [ $file_errors -eq 0 ]; then
        log_success "$filename is valid"
        ((valid_files++))
    else
        log_error "$filename has $file_errors issue(s)"
    fi

    return $file_errors
}

# Main validation function
main() {
    log_section "XHTML Validation Subagent"

    log_info "Working directory: $REBRANDED_DIR"
    cd "$REBRANDED_DIR"

    # Check for xmllint
    check_xmllint

    log_section "Validating XHTML Files"

    # Validate xhtml directory files
    if [ -d "xhtml" ]; then
        log_info "Validating files in xhtml/ directory..."
        for file in xhtml/*.xhtml; do
            if [ -f "$file" ]; then
                validate_xhtml_file "$file" || true
            fi
        done
    else
        log_warning "xhtml/ directory not found"
    fi

    # Validate templates directory files
    if [ -d "templates" ]; then
        log_info "Validating files in templates/ directory..."
        for file in templates/*.xhtml; do
            if [ -f "$file" ]; then
                validate_xhtml_file "$file" || true
            fi
        done
    else
        log_warning "templates/ directory not found"
    fi

    # Summary
    log_section "Validation Summary"

    echo -e "Total files processed: ${CYAN}$total_files${NC}"
    echo -e "Valid files: ${GREEN}$valid_files${NC}"
    echo -e "Files with errors: ${RED}$error_files${NC}"
    echo -e "Total warnings: ${YELLOW}$warning_count${NC}"

    if [ $error_files -eq 0 ]; then
        log_section "✅ All XHTML files are valid!"
        return 0
    else
        log_section "❌ Validation completed with errors"
        return 1
    fi
}

# Run main function
main "$@"
