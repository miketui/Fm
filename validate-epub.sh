#!/bin/bash

# EPUB Validation Script
# This script validates the EPUB structure and content

set -euo pipefail  # Enhanced error handling

# Color codes for better output
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m' # No Color

# Logging functions
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

# Error handler
error_handler() {
    local exit_code=$?
    local line_number=$1
    log_error "Script failed at line $line_number with exit code $exit_code"
    cleanup_temp
    exit $exit_code
}

trap 'error_handler $LINENO' ERR

# Cleanup function
cleanup_temp() {
    if [ -n "${TEMP_DIR:-}" ] && [ -d "$TEMP_DIR" ]; then
        log_info "Cleaning up temporary directory: $TEMP_DIR"
        rm -rf "$TEMP_DIR"
    fi
}

log_info "Starting EPUB validation..."
readonly ORIG_DIR="$PWD"

# Check if epubcheck is available
check_epubcheck() {
    if command -v epubcheck &> /dev/null; then
        log_success "epubcheck CLI found"
        return 0
    elif [ -f "epubcheck/epubcheck.jar" ] && command -v java &> /dev/null; then
        log_success "Using bundled epubcheck.jar"
        return 0
    elif command -v npx &> /dev/null && npx epubcheck --version &> /dev/null; then
        log_success "epubcheck available via npx"
        return 0
    elif command -v npm &> /dev/null; then
        log_warning "epubcheck not found. Installing via npm..."
        if npm install -g epubcheck; then
            log_success "epubcheck installed successfully"
            return 0
        else
            log_error "Failed to install epubcheck via npm"
            return 1
        fi
    else
        log_error "No epubcheck available and npm not installed. Please install Java or Node."
        return 1
    fi
}

if ! check_epubcheck; then
    exit 1
fi

# Create temporary EPUB structure for validation
TEMP_DIR=$(mktemp -d)
readonly EPUB_DIR="$TEMP_DIR/epub"

create_epub_structure() {
    log_info "Creating EPUB structure in $EPUB_DIR..."
    
    mkdir -p "$EPUB_DIR/OEBPS"
    mkdir -p "$EPUB_DIR/META-INF"

    # Copy content files with proper error handling
    if [ -d "OEBPS" ]; then
        log_info "Copying OEBPS directory structure..."
        cp -r OEBPS/* "$EPUB_DIR/OEBPS/" || {
            log_error "Failed to copy OEBPS content"
            return 1
        }
    else
        log_warning "OEBPS directory not found, checking for legacy structure..."
        # Fallback for legacy structure
        cp *.xhtml "$EPUB_DIR/OEBPS/" 2>/dev/null || log_warning "No XHTML files found in root"
        [ -d "styles" ] && cp -r styles "$EPUB_DIR/OEBPS/" || log_warning "No styles directory found"
        [ -d "images" ] && cp -r images "$EPUB_DIR/OEBPS/" || log_warning "No images directory found"
        [ -f "content.opf" ] && cp content.opf "$EPUB_DIR/OEBPS/" || log_warning "No content.opf found in root"
    fi
}

if ! create_epub_structure; then
    cleanup_temp
    exit 1
fi

# Create mimetype file
printf 'application/epub+zip' > "$EPUB_DIR/mimetype"

# Create container.xml if it doesn't exist
if [ ! -f "$EPUB_DIR/META-INF/container.xml" ]; then
    cat > "$EPUB_DIR/META-INF/container.xml" << 'EOF'
<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
EOF
fi

# Create ZIP package for validation
cd "$TEMP_DIR"
log_info "Creating EPUB package with proper structure..."

# Remove any existing epub.epub
rm -f epub.epub

if command -v zip &>/dev/null; then
    # First, add mimetype (uncompressed, first in archive)
    (cd epub && zip -0 -X ../epub.epub mimetype && zip -r ../epub.epub META-INF/ && zip -r ../epub.epub OEBPS/)
else
    if command -v python3 &>/dev/null; then
        log_info "zip not found; using python3 zipfile fallback"
        python3 - << 'PY'
import os, zipfile
base = 'epub'
out = 'epub.epub'
with zipfile.ZipFile(out, 'w') as z:
    # mimetype first, stored
    z.write(os.path.join(base, 'mimetype'), arcname='mimetype', compress_type=zipfile.ZIP_STORED)
    # add META-INF and OEBPS recursively
    for top in ('META-INF', 'OEBPS'):
        for root, _, files in os.walk(os.path.join(base, top)):
            for f in files:
                p = os.path.join(root, f)
                arc = os.path.relpath(p, base)
                if arc == 'mimetype':
                    continue
                z.write(p, arcname=arc, compress_type=zipfile.ZIP_DEFLATED)
PY
    else
        log_error "Neither 'zip' nor 'python3' available to create EPUB archive"
        cleanup_temp
        exit 1
    fi
fi

# Validate the EPUB
run_epubcheck_validation() {
    log_info "Running epubcheck validation..."
    
    local epub_cmd
    if [ -f "epubcheck/epubcheck.jar" ] && command -v java &> /dev/null; then
        epub_cmd="java -jar \"$PWD/epubcheck/epubcheck.jar\""
    elif command -v epubcheck &> /dev/null; then
        epub_cmd="epubcheck"
    else
        epub_cmd="npx epubcheck"
    fi
    
    local validation_output
    if [ -f "$ORIG_DIR/epubcheck/epubcheck.jar" ] && command -v java &> /dev/null; then
        if validation_output=$(java -jar "$ORIG_DIR/epubcheck/epubcheck.jar" epub.epub 2>&1); then
            log_success "EPUB validation passed!"
            echo "$validation_output" | grep -E "(INFO|HINT|USAGE)" || true
            return 0
        else
            log_error "EPUB validation failed!"
            echo "$validation_output"
            return 1
        fi
    elif command -v epubcheck &> /dev/null; then
        if validation_output=$(epubcheck epub.epub 2>&1); then
            log_success "EPUB validation passed!"
            echo "$validation_output" | grep -E "(INFO|HINT|USAGE)" || true
            return 0
        else
            log_error "EPUB validation failed!"
            echo "$validation_output"
            return 1
        fi
    else
        if validation_output=$(npx epubcheck epub.epub 2>&1); then
            log_success "EPUB validation passed!"
            echo "$validation_output" | grep -E "(INFO|HINT|USAGE)" || true
            return 0
        else
            log_error "EPUB validation failed!"
            echo "$validation_output"
            return 1
        fi
    fi
}

if run_epubcheck_validation; then
    VALIDATION_RESULT=0
else
    VALIDATION_RESULT=1
fi

# Return to original directory and cleanup
cd - > /dev/null
cleanup_temp

# Additional HTML validation with better error handling
run_additional_validation() {
    log_info "Running additional HTML validation..."
    
    local xhtml_files
    if [ -d "OEBPS/text" ]; then
        xhtml_files="OEBPS/text/*.xhtml"
    else
        xhtml_files="*.xhtml"
    fi
    
    # Check for common EPUB issues
    log_info "Checking for missing alt attributes..."
    local missing_alt
    if missing_alt=$(find $xhtml_files -type f 2>/dev/null | xargs grep -l 'img.*src=' 2>/dev/null | xargs grep 'img.*src=' 2>/dev/null | grep -v 'alt=' || true); then
        if [ -n "$missing_alt" ]; then
            log_warning "Found images without alt attributes:"
            echo "$missing_alt"
        else
            log_success "All images have alt attributes"
        fi
    fi
    
    log_info "Checking for proper EPUB namespaces..."
    local missing_epub_ns
    if missing_epub_ns=$(find $xhtml_files -type f 2>/dev/null | xargs grep -L 'xmlns:epub="http://www.idpf.org/2007/ops"' 2>/dev/null || true); then
        if [ -n "$missing_epub_ns" ]; then
            log_warning "Files missing EPUB namespace:"
            echo "$missing_epub_ns"
        else
            log_success "All files have proper EPUB namespace"
        fi
    fi
    
    log_info "Checking for consistent DOCTYPE declarations..."
    local inconsistent_doctype
    if inconsistent_doctype=$(find $xhtml_files -type f 2>/dev/null | xargs grep -L '<!DOCTYPE html>' 2>/dev/null || true); then
        if [ -n "$inconsistent_doctype" ]; then
            log_warning "Files with inconsistent DOCTYPE:"
            echo "$inconsistent_doctype"
        else
            log_success "All files have consistent DOCTYPE"
        fi
    fi
    
    log_success "Additional validation checks completed"
}

run_additional_validation

exit $VALIDATION_RESULT
