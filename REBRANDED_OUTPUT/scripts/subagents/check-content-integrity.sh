#!/bin/bash
# Content Integrity Check Subagent
# Verifies all content files are present, properly referenced, and maintain data integrity

set -euo pipefail

# Color codes
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly CYAN='\033[0;36m'
readonly NC='\033[0m'

# Counters
errors=0
warnings=0

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
    ((warnings++))
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
    ((errors++))
}

log_section() {
    echo -e "\n${CYAN}═══════════════════════════════════════════${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════${NC}\n"
}

# Check expected file counts
check_file_counts() {
    log_section "Checking File Counts"

    # Count XHTML files in xhtml directory
    if [ -d "xhtml" ]; then
        local xhtml_count=$(find xhtml -name "*.xhtml" | wc -l)
        log_info "XHTML files in xhtml/: $xhtml_count"

        # Expected: 46 files (per README)
        if [ $xhtml_count -lt 40 ]; then
            log_warning "Expected approximately 46 XHTML files, found $xhtml_count"
        else
            log_success "XHTML file count looks good"
        fi
    else
        log_error "xhtml/ directory not found"
    fi

    # Count images
    if [ -d "images" ]; then
        local image_count=$(find images -type f | wc -l)
        log_info "Image files: $image_count"

        # Expected: 31 images (per README)
        if [ $image_count -lt 30 ]; then
            log_warning "Expected approximately 31 images, found $image_count"
        else
            log_success "Image file count looks good"
        fi
    else
        log_error "images/ directory not found"
    fi

    # Count fonts
    if [ -d "fonts" ]; then
        local font_count=$(find fonts -type f | wc -l)
        log_info "Font files: $font_count"

        # Expected: 6 fonts (per README)
        if [ $font_count -ne 6 ]; then
            log_warning "Expected 6 fonts, found $font_count"
        else
            log_success "Font file count correct (6 fonts)"
        fi
    else
        log_error "fonts/ directory not found"
    fi
}

# Check chapters are present
check_chapters() {
    log_section "Checking Chapter Files"

    local expected_chapters=(
        "chapter-i-unveiling-your-creative-odyssey"
        "chapter-ii-refining-your-creative-toolkit"
        "chapter-iii-reigniting-your-creative-fire"
        "chapter-iv-the-art-of-networking-in-freelance-hairstyling"
        "chapter-v-cultivating-creative-excellence-through-mentorship"
        "chapter-vi-mastering-the-business-of-hairstyling"
        "chapter-vii-embracing-wellness-and-self-care"
        "chapter-viii-advancing-skills-through-continuous-education"
        "chapter-ix-stepping-into-leadership"
        "chapter-x-crafting-enduring-legacies"
        "chapter-xi-advanced-digital-strategies-for-freelance-hairstylists"
        "chapter-xii-financial-wisdom-building-sustainable-ventures"
        "chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling"
        "chapter-xiv-the-impact-of-ai-on-the-beauty-industry"
        "chapter-xv-cultivating-resilience-and-well-being-in-hairstyling"
        "chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling"
    )

    local missing_chapters=0

    for chapter in "${expected_chapters[@]}"; do
        # Check for various possible filenames
        if [ -f "xhtml/${chapter}.xhtml" ] || \
           [ -f "xhtml/9-${chapter}.xhtml" ] || \
           [ -f "xhtml/10-${chapter}.xhtml" ] || \
           [ -f "xhtml/11-${chapter}.xhtml" ] || \
           ls xhtml/*${chapter}*.xhtml 2>/dev/null | grep -q .; then
            log_success "Found: $chapter"
        else
            log_error "Missing: $chapter"
            ((missing_chapters++))
        fi
    done

    if [ $missing_chapters -eq 0 ]; then
        log_success "All 16 chapters present"
    else
        log_error "$missing_chapters chapter(s) missing"
    fi
}

# Check frontmatter and backmatter
check_matter_files() {
    log_section "Checking Frontmatter and Backmatter"

    # Expected frontmatter files
    local frontmatter=(
        "TitlePage"
        "Copyright"
        "Dedication"
        "TableOfContents"
        "SelfAssessment"
        "AffirmationOdyssey"
        "Preface"
    )

    log_info "Checking frontmatter files..."
    for file in "${frontmatter[@]}"; do
        if ls xhtml/*${file}*.xhtml 2>/dev/null | grep -q .; then
            log_success "Found: $file"
        else
            log_warning "Frontmatter may be missing: $file"
        fi
    done

    # Check for key backmatter files
    local backmatter=(
        "Conclusion"
        "QuizKey"
        "SelfAssessment"
        "Acknowledgments"
        "AbouttheAuthor"
    )

    log_info "Checking backmatter files..."
    for file in "${backmatter[@]}"; do
        if ls xhtml/*${file}*.xhtml 2>/dev/null | grep -q .; then
            log_success "Found: $file"
        else
            log_warning "Backmatter may be missing: $file"
        fi
    done
}

# Check image references
check_image_references() {
    log_section "Checking Image References"

    log_info "Scanning XHTML files for image references..."

    local broken_refs=0

    for xhtml_file in xhtml/*.xhtml templates/*.xhtml 2>/dev/null; do
        if [ ! -f "$xhtml_file" ]; then
            continue
        fi

        # Extract image src attributes
        while IFS= read -r line; do
            if [[ $line =~ src=\"([^\"]+)\" ]] || [[ $line =~ src=\'([^\']+)\' ]]; then
                local img_path="${BASH_REMATCH[1]}"

                # Skip external URLs
                if [[ $img_path =~ ^http ]]; then
                    continue
                fi

                # Resolve relative path
                local resolved_path="$img_path"

                # Check if image exists
                if [ ! -f "$resolved_path" ]; then
                    # Try alternative paths
                    if [ -f "images/$(basename "$img_path")" ]; then
                        resolved_path="images/$(basename "$img_path")"
                    elif [ -f "../images/$(basename "$img_path")" ]; then
                        resolved_path="../images/$(basename "$img_path")"
                    else
                        log_error "Broken image reference in $(basename "$xhtml_file"): $img_path"
                        ((broken_refs++))
                    fi
                fi
            fi
        done < <(grep -o '<img[^>]*>' "$xhtml_file" 2>/dev/null || true)
    done

    if [ $broken_refs -eq 0 ]; then
        log_success "All image references are valid"
    else
        log_error "Found $broken_refs broken image reference(s)"
    fi
}

# Check CSS references
check_css_references() {
    log_section "Checking CSS References"

    log_info "Scanning XHTML files for CSS references..."

    local broken_refs=0

    for xhtml_file in xhtml/*.xhtml templates/*.xhtml 2>/dev/null; do
        if [ ! -f "$xhtml_file" ]; then
            continue
        fi

        # Extract CSS href attributes
        while IFS= read -r line; do
            if [[ $line =~ href=\"([^\"]+\.css)\" ]]; then
                local css_path="${BASH_REMATCH[1]}"

                # Check if CSS file exists
                if [ ! -f "$css_path" ]; then
                    log_warning "CSS reference in $(basename "$xhtml_file"): $css_path not found"
                    ((broken_refs++))
                fi
            fi
        done < <(grep 'stylesheet' "$xhtml_file" 2>/dev/null || true)
    done

    if [ $broken_refs -eq 0 ]; then
        log_success "All CSS references are valid"
    else
        log_warning "Found $broken_refs CSS reference issue(s)"
    fi
}

# Check internal links
check_internal_links() {
    log_section "Checking Internal Links"

    log_info "Scanning for internal XHTML links..."

    local broken_links=0

    for xhtml_file in xhtml/*.xhtml templates/*.xhtml 2>/dev/null; do
        if [ ! -f "$xhtml_file" ]; then
            continue
        fi

        # Extract internal links (href to .xhtml files)
        while IFS= read -r line; do
            if [[ $line =~ href=\"([^\"]+\.xhtml[^\"]*)\" ]]; then
                local link="${BASH_REMATCH[1]}"

                # Remove anchor if present
                local file_only="${link%%#*}"

                # Skip external links
                if [[ $file_only =~ ^http ]]; then
                    continue
                fi

                # Check if file exists
                if [ -n "$file_only" ] && [ ! -f "$file_only" ] && [ ! -f "xhtml/$file_only" ]; then
                    log_warning "Broken internal link in $(basename "$xhtml_file"): $link"
                    ((broken_links++))
                fi
            fi
        done < <(grep -o 'href="[^"]*\.xhtml[^"]*"' "$xhtml_file" 2>/dev/null || true)
    done

    if [ $broken_links -eq 0 ]; then
        log_success "All internal links appear valid"
    else
        log_warning "Found $broken_links potential broken link(s)"
    fi
}

# Main function
main() {
    log_section "Content Integrity Check Subagent"

    log_info "Working directory: $REBRANDED_DIR"
    cd "$REBRANDED_DIR"

    # Run all checks
    check_file_counts
    check_chapters
    check_matter_files
    check_image_references
    check_css_references
    check_internal_links

    # Summary
    log_section "Integrity Check Summary"

    echo -e "Errors: ${RED}$errors${NC}"
    echo -e "Warnings: ${YELLOW}$warnings${NC}"

    if [ $errors -eq 0 ] && [ $warnings -eq 0 ]; then
        log_section "✅ Content integrity verified - all checks passed!"
        return 0
    elif [ $errors -eq 0 ]; then
        log_section "✅ Content integrity verified with minor warnings"
        return 0
    else
        log_section "❌ Content integrity issues found"
        return 1
    fi
}

# Run main function
main "$@"
