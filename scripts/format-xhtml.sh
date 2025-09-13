#!/bin/bash

# XHTML Formatting Script
# Ensures consistent formatting for XHTML files in EPUB

set -euo pipefail

# Color codes
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
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

# Format a single XHTML file
format_xhtml_file() {
    local file="$1"
    local temp_file="${file}.tmp"
    local changes_made=false
    
    log_info "Formatting $file..."
    
    # Read the file
    if [ ! -f "$file" ]; then
        log_error "File not found: $file"
        return 1
    fi
    
    # Create formatted version
    {
        # Process line by line
        while IFS= read -r line; do
            # Skip empty lines at the beginning
            if [[ -z "$line" && "$changes_made" == false ]]; then
                continue
            fi
            changes_made=true
            
            # Remove trailing whitespace
            line="${line%"${line##*[![:space:]]}"}"
            
            # Fix common formatting issues
            # Add space after commas in attributes
            line=$(echo "$line" | sed 's/,\([^[:space:]]\)/, \1/g')
            
            # Ensure proper spacing around = in attributes
            line=$(echo "$line" | sed 's/\([^[:space:]]\)=\([^[:space:]]\)/\1="\2/g')
            line=$(echo "$line" | sed 's/=\([^"[:space:]]\)/="\1/g')
            
            # Fix self-closing tags
            line=$(echo "$line" | sed 's|<\([^>]*[^/]\)>|<\1/>|g' | sed 's|<\([^>]*\)//|<\1/|g')
            
            echo "$line"
        done < "$file"
    } > "$temp_file"
    
    # Check if changes were made
    if ! cmp -s "$file" "$temp_file"; then
        mv "$temp_file" "$file"
        log_success "Formatted $file"
        return 0
    else
        rm "$temp_file"
        log_info "No changes needed for $file"
        return 0
    fi
}

# Validate XHTML structure
validate_xhtml_structure() {
    local file="$1"
    local errors=()
    
    # Check for XML declaration
    if ! head -1 "$file" | grep -q '<?xml version="1.0"'; then
        errors+=("Missing XML declaration")
    fi
    
    # Check for DOCTYPE
    if ! grep -q '<!DOCTYPE html>' "$file"; then
        errors+=("Missing DOCTYPE declaration")
    fi
    
    # Check for XHTML namespace
    if ! grep -q 'xmlns="http://www.w3.org/1999/xhtml"' "$file"; then
        errors+=("Missing XHTML namespace")
    fi
    
    # Check for basic structure
    if ! grep -q '<html' "$file"; then
        errors+=("Missing html element")
    fi
    
    if ! grep -q '<head>' "$file"; then
        errors+=("Missing head element")
    fi
    
    if ! grep -q '<body>' "$file"; then
        errors+=("Missing body element")
    fi
    
    # Report errors
    if [ ${#errors[@]} -gt 0 ]; then
        log_error "Structure issues in $file:"
        for error in "${errors[@]}"; do
            echo "  • $error"
        done
        return 1
    fi
    
    return 0
}

# Main processing function
process_xhtml_files() {
    local files=()
    local format_errors=0
    local validation_errors=0
    
    # Find XHTML files
    if [ $# -eq 0 ]; then
        # Process all XHTML files
        if [ -d "OEBPS/text" ]; then
            mapfile -t files < <(find OEBPS/text -name "*.xhtml" -type f)
        else
            mapfile -t files < <(find . -name "*.xhtml" -type f -maxdepth 1)
        fi
    else
        # Process specified files
        files=("$@")
    fi
    
    if [ ${#files[@]} -eq 0 ]; then
        log_warning "No XHTML files found to process"
        return 0
    fi
    
    log_info "Processing ${#files[@]} XHTML files..."
    
    # Format each file
    for file in "${files[@]}"; do
        if format_xhtml_file "$file"; then
            if ! validate_xhtml_structure "$file"; then
                ((validation_errors++))
            fi
        else
            ((format_errors++))
        fi
    done
    
    # Report results
    if [ $format_errors -eq 0 ] && [ $validation_errors -eq 0 ]; then
        log_success "All XHTML files processed successfully"
        return 0
    else
        if [ $format_errors -gt 0 ]; then
            log_error "$format_errors files had formatting errors"
        fi
        if [ $validation_errors -gt 0 ]; then
            log_error "$validation_errors files had validation errors"
        fi
        return 1
    fi
}

# Main execution
if [ "${BASH_SOURCE[0]}" == "${0}" ]; then
    log_info "Starting XHTML formatting..."
    
    if process_xhtml_files "$@"; then
        log_success "XHTML formatting completed successfully"
        exit 0
    else
        log_error "XHTML formatting completed with errors"
        exit 1
    fi
fi