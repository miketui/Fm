#!/bin/bash
# EPUB Package Validation Subagent
# Validates EPUB package structure, manifest, spine, and metadata

set -euo pipefail

# Color codes
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly CYAN='\033[0;36m'
readonly NC='\033[0m'

# Counters
error_count=0
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
    ((error_count++))
}

log_section() {
    echo -e "\n${CYAN}═══════════════════════════════════════════${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════${NC}\n"
}

# Check if file exists
check_file() {
    local file="$1"
    local description="$2"

    if [ -f "$file" ]; then
        log_success "$description found: $file"
        return 0
    else
        log_error "$description not found: $file"
        return 1
    fi
}

# Validate mimetype file
validate_mimetype() {
    log_section "Validating mimetype"

    if check_file "mimetype" "Mimetype file"; then
        local content=$(cat mimetype)
        if [ "$content" = "application/epub+zip" ]; then
            log_success "Mimetype content is correct"
        else
            log_error "Mimetype content incorrect. Expected 'application/epub+zip', got '$content'"
        fi
    fi
}

# Validate container.xml
validate_container() {
    log_section "Validating META-INF/container.xml"

    if check_file "META-INF/container.xml" "Container file"; then
        # Check for required elements
        if grep -q '<container' META-INF/container.xml && \
           grep -q '<rootfiles' META-INF/container.xml && \
           grep -q 'full-path=' META-INF/container.xml; then
            log_success "Container structure is valid"

            # Extract and verify OPF path
            local opf_path=$(grep 'full-path=' META-INF/container.xml | sed 's/.*full-path="\([^"]*\)".*/\1/')
            log_info "OPF path declared as: $opf_path"

            if [ -f "$opf_path" ]; then
                log_success "OPF file exists at declared path"
            else
                log_error "OPF file not found at declared path: $opf_path"
            fi
        else
            log_error "Container structure is invalid or incomplete"
        fi

        # Validate XML structure
        if command -v xmllint &> /dev/null; then
            if xmllint --noout META-INF/container.xml 2>/dev/null; then
                log_success "Container XML is well-formed"
            else
                log_error "Container XML has syntax errors"
            fi
        fi
    fi
}

# Validate content.opf
validate_content_opf() {
    log_section "Validating content.opf"

    if check_file "content.opf" "Package document (content.opf)"; then
        # Validate XML structure
        if command -v xmllint &> /dev/null; then
            if xmllint --noout content.opf 2>/dev/null; then
                log_success "OPF XML is well-formed"
            else
                log_error "OPF XML has syntax errors"
                xmllint --noout content.opf 2>&1 | head -5
                return 1
            fi
        fi

        # Check required metadata
        log_info "Checking required metadata..."

        if grep -q '<dc:title' content.opf; then
            log_success "Title metadata present"
        else
            log_error "Title metadata missing"
        fi

        if grep -q '<dc:language' content.opf; then
            log_success "Language metadata present"
        else
            log_error "Language metadata missing"
        fi

        if grep -q '<dc:identifier' content.opf; then
            log_success "Identifier metadata present"
        else
            log_error "Identifier metadata missing"
        fi

        # Check manifest
        log_info "Checking manifest..."

        if grep -q '<manifest' content.opf; then
            local manifest_items=$(grep -o '<item ' content.opf | wc -l)
            log_success "Manifest contains $manifest_items items"

            # Verify navigation document is declared
            if grep -q 'properties="nav"' content.opf; then
                log_success "Navigation document declared in manifest"
            else
                log_warning "Navigation document may not be properly declared"
            fi
        else
            log_error "Manifest section missing"
        fi

        # Check spine
        log_info "Checking spine..."

        if grep -q '<spine' content.opf; then
            local spine_items=$(grep -o '<itemref ' content.opf | wc -l)
            log_success "Spine contains $spine_items items"
        else
            log_error "Spine section missing"
        fi

        # Verify files in manifest exist
        log_info "Verifying manifest files exist..."
        validate_manifest_files
    fi
}

# Validate manifest files exist
validate_manifest_files() {
    local missing_files=0

    # Extract hrefs from manifest (simplified)
    while IFS= read -r line; do
        if [[ $line =~ href=\"([^\"]+)\" ]]; then
            local href="${BASH_REMATCH[1]}"
            if [ ! -f "$href" ]; then
                log_warning "Manifest file not found: $href"
                ((missing_files++))
            fi
        fi
    done < <(grep '<item ' content.opf)

    if [ $missing_files -eq 0 ]; then
        log_success "All manifest files exist"
    else
        log_error "$missing_files manifest files are missing"
    fi
}

# Validate navigation document
validate_navigation() {
    log_section "Validating Navigation Document"

    if [ -f "xhtml/nav.xhtml" ]; then
        log_success "Navigation file found: xhtml/nav.xhtml"

        # Check for nav element
        if grep -q '<nav' xhtml/nav.xhtml && grep -q 'epub:type="toc"' xhtml/nav.xhtml; then
            log_success "Navigation structure is valid"
        else
            log_warning "Navigation structure may be incomplete"
        fi

        # Validate XML
        if command -v xmllint &> /dev/null; then
            if xmllint --noout xhtml/nav.xhtml 2>/dev/null; then
                log_success "Navigation XML is well-formed"
            else
                log_error "Navigation XML has syntax errors"
            fi
        fi
    else
        log_error "Navigation file not found: xhtml/nav.xhtml"
    fi
}

# Check directory structure
validate_directory_structure() {
    log_section "Validating Directory Structure"

    local required_dirs=("xhtml" "images" "fonts" "styles" "META-INF")

    for dir in "${required_dirs[@]}"; do
        if [ -d "$dir" ]; then
            local file_count=$(find "$dir" -type f | wc -l)
            log_success "Directory '$dir' exists with $file_count files"
        else
            log_warning "Directory '$dir' not found"
        fi
    done
}

# Main validation function
main() {
    log_section "EPUB Package Validation Subagent"

    log_info "Working directory: $REBRANDED_DIR"
    cd "$REBRANDED_DIR"

    # Run all validations
    validate_mimetype
    validate_container
    validate_content_opf
    validate_navigation
    validate_directory_structure

    # Summary
    log_section "Package Validation Summary"

    echo -e "Errors: ${RED}$error_count${NC}"
    echo -e "Warnings: ${YELLOW}$warning_count${NC}"

    if [ $error_count -eq 0 ]; then
        log_section "✅ EPUB package structure is valid!"
        return 0
    else
        log_section "❌ EPUB package has errors that need to be fixed"
        return 1
    fi
}

# Run main function
main "$@"
