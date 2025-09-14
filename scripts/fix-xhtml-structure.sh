#!/bin/bash

# XHTML Structure Fix Script
# Fixes all structural issues found in XHTML files for EPUB compliance

set -euo pipefail

# Color codes
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m'

log_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }

# Counter for fixed files
FIXED_COUNT=0
TOTAL_FILES=0

fix_xhtml_file() {
    local file="$1"
    local backup_file="${file}.backup"
    
    TOTAL_FILES=$((TOTAL_FILES + 1))
    log_info "Processing $file..."
    
    # Create backup
    cp "$file" "$backup_file"
    
    # Read the file content
    local content
    content=$(<"$file")
    
    # Fix common XHTML structure issues
    local fixed_content
    
    # 1. Fix XML declaration (if malformed)
    if [[ $content =~ ^\<\?xml.*version=\"\".*\?\> ]]; then
        log_warning "Fixing malformed XML declaration in $file"
        fixed_content=$(echo "$content" | sed 's/<?xml version=""/<?xml version="1.0"/')
        content="$fixed_content"
    fi
    
    # 2. Fix DOCTYPE declaration
    if [[ $content =~ ^\<\!DOCTYPE\ html/\> ]]; then
        log_warning "Fixing malformed DOCTYPE in $file"
        fixed_content=$(echo "$content" | sed 's|<!DOCTYPE html/>|<!DOCTYPE html>|')
        content="$fixed_content"
    fi
    
    # 3. Fix HTML opening tag with malformed namespaces
    if [[ $content =~ \<html.*xmlns=\"\".*\> ]]; then
        log_warning "Fixing malformed namespaces in $file"
        # Fix malformed namespace declarations
        fixed_content=$(echo "$content" | sed 's/xmlns=""/xmlns=/g')
        fixed_content=$(echo "$fixed_content" | sed 's/xmlns:epub=""/xmlns:epub=/g')
        fixed_content=$(echo "$fixed_content" | sed 's/lang=""/lang=/g')
        fixed_content=$(echo "$fixed_content" | sed 's/xml:lang=""/xml:lang=/g')
        content="$fixed_content"
    fi
    
    # 4. Fix self-closing tags that should be properly closed
    local tags=("head" "title" "style" "body" "html")
    for tag in "${tags[@]}"; do
        if [[ $content =~ \<$tag.*\/\> ]]; then
            log_warning "Fixing self-closing $tag tag in $file"
            fixed_content=$(echo "$content" | sed "s|<$tag\([^>]*\)/>|<$tag\1></$tag>|g")
            content="$fixed_content"
        fi
    done
    
    # 5. Add proper XML declaration if missing
    if ! [[ $content =~ ^\<\?xml ]]; then
        log_warning "Adding XML declaration to $file"
        content="<?xml version=\"1.0\" encoding=\"UTF-8\"?>
$content"
    fi
    
    # 6. Add proper DOCTYPE if missing
    if ! [[ $content =~ \<\!DOCTYPE ]]; then
        log_warning "Adding DOCTYPE to $file"
        content="${content//<html/<!DOCTYPE html>
<html}"
    fi
    
    # 7. Ensure proper XHTML namespace
    if ! [[ $content =~ xmlns=\"http://www\.w3\.org/1999/xhtml\" ]]; then
        log_warning "Adding XHTML namespace to $file"
        content="${content//xmlns=/xmlns=\"http://www.w3.org/1999/xhtml\" }"
    fi
    
    # 8. Ensure proper EPUB namespace
    if ! [[ $content =~ xmlns:epub=\"http://www\.idpf\.org/2007/ops\" ]]; then
        log_warning "Adding EPUB namespace to $file"
        content="${content//xmlns:epub=/xmlns:epub=\"http://www.idpf.org/2007/ops\" }"
    fi
    
    # 9. Fix language attributes
    if [[ $content =~ lang=.*en.*xml:lang= ]]; then
        log_warning "Fixing language attributes in $file"
        content="${content//lang=/lang=\"en\" }"
        content="${content//xml:lang=/xml:lang=\"en\" }"
    fi
    
    # Write the fixed content back
    echo "$content" > "$file"
    
    # Validate the fix by checking for basic structure
    if [[ $content =~ \<\?xml.*version=\"1\.0\" ]] && 
       [[ $content =~ \<\!DOCTYPE\ html\> ]] && 
       [[ $content =~ xmlns=\"http://www\.w3\.org/1999/xhtml\" ]]; then
        FIXED_COUNT=$((FIXED_COUNT + 1))
        log_success "Fixed XHTML structure in $file"
        rm "$backup_file"  # Remove backup if successful
    else
        log_error "Failed to fix $file, restoring backup"
        mv "$backup_file" "$file"
    fi
}

main() {
    log_info "🔧 Starting XHTML Structure Fix for EPUB Compliance"
    
    # Check if OEBPS/text directory exists
    if [[ ! -d "OEBPS/text" ]]; then
        log_error "OEBPS/text directory not found. Run from EPUB project root."
        exit 1
    fi
    
    # Process all XHTML files
    while IFS= read -r -d '' file; do
        fix_xhtml_file "$file"
    done < <(find OEBPS/text -name "*.xhtml" -print0)
    
    log_success "🎉 XHTML Structure Fix Complete!"
    log_success "📊 Fixed $FIXED_COUNT out of $TOTAL_FILES files"
    
    if [[ $FIXED_COUNT -eq $TOTAL_FILES ]]; then
        log_success "✅ All XHTML files are now EPUB compliant!"
        log_info "🔍 Run 'npm run validate' to verify the fixes"
    else
        log_warning "⚠️  Some files may need manual review"
        log_info "🔍 Check the validation output for remaining issues"
    fi
}

main "$@"