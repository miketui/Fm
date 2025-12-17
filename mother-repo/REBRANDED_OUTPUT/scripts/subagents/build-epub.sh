#!/bin/bash
# EPUB Build Subagent
# Builds production-ready EPUB file from REBRANDED_OUTPUT directory

set -euo pipefail

# Color codes
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly CYAN='\033[0;36m'
readonly MAGENTA='\033[0;35m'
readonly NC='\033[0m'

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REBRANDED_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# EPUB filename
EPUB_FILE="The-Artisans-Path.epub"

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

log_section() {
    echo -e "\n${CYAN}═══════════════════════════════════════════${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════${NC}\n"
}

log_step() {
    echo -e "${MAGENTA}▶ $1${NC}"
}

# Check if zip is available
check_zip() {
    if command -v zip &> /dev/null; then
        log_success "zip utility found"
        return 0
    else
        log_error "zip utility not found. Please install zip."
        return 1
    fi
}

# Pre-build validation
pre_build_checks() {
    log_section "Pre-Build Validation"

    local errors=0

    # Check required files
    log_info "Checking required files..."

    local required_files=(
        "mimetype"
        "META-INF/container.xml"
        "content.opf"
    )

    for file in "${required_files[@]}"; do
        if [ -f "$file" ]; then
            log_success "Found: $file"
        else
            log_error "Missing: $file"
            ((errors++))
        fi
    done

    # Check required directories
    log_info "Checking required directories..."

    local required_dirs=("xhtml" "images" "fonts" "styles")

    for dir in "${required_dirs[@]}"; do
        if [ -d "$dir" ]; then
            local count=$(find "$dir" -type f | wc -l)
            log_success "Found: $dir ($count files)"
        else
            log_error "Missing: $dir"
            ((errors++))
        fi
    done

    if [ $errors -eq 0 ]; then
        log_success "Pre-build checks passed"
        return 0
    else
        log_error "Pre-build checks failed with $errors error(s)"
        return 1
    fi
}

# Clean old EPUB file
clean_old_epub() {
    log_section "Cleaning Old Build"

    if [ -f "$EPUB_FILE" ]; then
        log_info "Removing old EPUB file: $EPUB_FILE"
        rm -f "$EPUB_FILE"
        log_success "Old EPUB file removed"
    else
        log_info "No old EPUB file to remove"
    fi
}

# Build EPUB package
build_epub_package() {
    log_section "Building EPUB Package"

    log_step "Step 1: Adding mimetype (uncompressed)"
    if zip -X -0 "$EPUB_FILE" mimetype; then
        log_success "Mimetype added (stored, no compression)"
    else
        log_error "Failed to add mimetype"
        return 1
    fi

    log_step "Step 2: Adding META-INF directory"
    if zip -X -r "$EPUB_FILE" META-INF; then
        log_success "META-INF directory added"
    else
        log_error "Failed to add META-INF"
        return 1
    fi

    log_step "Step 3: Adding content.opf"
    if zip -X -r "$EPUB_FILE" content.opf; then
        log_success "content.opf added"
    else
        log_error "Failed to add content.opf"
        return 1
    fi

    log_step "Step 4: Adding xhtml directory"
    if zip -X -r "$EPUB_FILE" xhtml; then
        local xhtml_count=$(find xhtml -name "*.xhtml" | wc -l)
        log_success "xhtml directory added ($xhtml_count files)"
    else
        log_error "Failed to add xhtml directory"
        return 1
    fi

    log_step "Step 5: Adding fonts directory"
    if zip -X -r "$EPUB_FILE" fonts; then
        local font_count=$(find fonts -type f | wc -l)
        log_success "fonts directory added ($font_count files)"
    else
        log_error "Failed to add fonts directory"
        return 1
    fi

    log_step "Step 6: Adding images directory"
    if zip -X -r "$EPUB_FILE" images; then
        local image_count=$(find images -type f | wc -l)
        log_success "images directory added ($image_count files)"
    else
        log_error "Failed to add images directory"
        return 1
    fi

    log_step "Step 7: Adding styles directory"
    if zip -X -r "$EPUB_FILE" styles; then
        log_success "styles directory added"
    else
        log_error "Failed to add styles directory"
        return 1
    fi

    # Add templates if exists
    if [ -d "templates" ]; then
        log_step "Step 8: Adding templates directory"
        if zip -X -r "$EPUB_FILE" templates; then
            local template_count=$(find templates -name "*.xhtml" | wc -l)
            log_success "templates directory added ($template_count files)"
        else
            log_warning "Failed to add templates directory (non-critical)"
        fi
    fi

    log_success "EPUB package created successfully"
}

# Verify EPUB structure
verify_epub_structure() {
    log_section "Verifying EPUB Structure"

    if [ ! -f "$EPUB_FILE" ]; then
        log_error "EPUB file not found: $EPUB_FILE"
        return 1
    fi

    # Get file size
    local file_size=$(du -h "$EPUB_FILE" | cut -f1)
    log_info "EPUB file size: $file_size"

    # List contents
    log_info "Verifying EPUB contents..."

    if unzip -l "$EPUB_FILE" > /dev/null 2>&1; then
        local total_files=$(unzip -l "$EPUB_FILE" | grep -c ".*" || true)
        log_success "EPUB archive is valid ($total_files entries)"

        # Check mimetype is first
        local first_file=$(unzip -l "$EPUB_FILE" | grep -m 1 "mimetype" || echo "")
        if [ -n "$first_file" ]; then
            log_success "mimetype is correctly positioned in archive"
        else
            log_warning "mimetype position could not be verified"
        fi
    else
        log_error "EPUB archive appears to be corrupted"
        return 1
    fi
}

# Generate build report
generate_build_report() {
    log_section "Build Report"

    if [ -f "$EPUB_FILE" ]; then
        local file_size=$(du -h "$EPUB_FILE" | cut -f1)
        local file_size_bytes=$(stat -c%s "$EPUB_FILE" 2>/dev/null || stat -f%z "$EPUB_FILE" 2>/dev/null)
        local entry_count=$(unzip -l "$EPUB_FILE" | tail -1 | awk '{print $2}')

        echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo -e "${GREEN}✅ EPUB BUILD SUCCESSFUL${NC}"
        echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo ""
        echo -e "  📦 Filename: ${CYAN}$EPUB_FILE${NC}"
        echo -e "  📊 Size: ${CYAN}$file_size${NC} (${file_size_bytes} bytes)"
        echo -e "  📄 Entries: ${CYAN}$entry_count${NC} files"
        echo -e "  📍 Location: ${CYAN}$REBRANDED_DIR/$EPUB_FILE${NC}"
        echo ""
        echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
        echo ""
        log_info "Next steps:"
        echo "  1. Validate with epubcheck"
        echo "  2. Test in ebook readers"
        echo "  3. Distribute to platforms"

        return 0
    else
        log_error "EPUB file was not created"
        return 1
    fi
}

# Main build function
main() {
    log_section "EPUB Build Subagent"

    log_info "Working directory: $REBRANDED_DIR"
    cd "$REBRANDED_DIR"

    # Check dependencies
    if ! check_zip; then
        exit 1
    fi

    # Run build process
    if ! pre_build_checks; then
        log_error "Pre-build validation failed. Fix errors and try again."
        exit 1
    fi

    clean_old_epub

    if ! build_epub_package; then
        log_error "EPUB build failed"
        exit 1
    fi

    if ! verify_epub_structure; then
        log_error "EPUB verification failed"
        exit 1
    fi

    generate_build_report

    log_section "✅ Build Complete!"
    exit 0
}

# Run main function
main "$@"
