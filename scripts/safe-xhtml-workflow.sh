#!/bin/bash

# Safe XHTML Validation and Fixing Workflow
# Implements proper safeguards for XHTML processing

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

# Parse command line arguments
DRY_RUN=false
FORCE=false
SKIP_BACKUP=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --force)
            FORCE=true
            shift
            ;;
        --skip-backup)
            SKIP_BACKUP=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [options]"
            echo "Options:"
            echo "  --dry-run       Show what would be fixed without making changes"
            echo "  --force         Skip confirmation prompts"
            echo "  --skip-backup   Skip creating backup (not recommended)"
            echo "  -h, --help      Show this help message"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

confirm_action() {
    if [[ "$FORCE" == "true" ]]; then
        return 0
    fi
    
    echo -n "$1 (y/N): "
    read -r response
    case "$response" in
        [yY][eE][sS]|[yY])
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

main() {
    log_info "🛡️  Safe XHTML Validation and Fixing Workflow"
    
    # Check if we're in the right directory
    if [[ ! -d "OEBPS/text" ]]; then
        log_error "OEBPS/text directory not found. Run from EPUB project root."
        exit 1
    fi
    
    # Step 1: Run validation to see current state
    log_info "🔍 Step 1: Running initial validation..."
    if ! node scripts/validate-xhtml-safe.js; then
        log_warning "Validation found issues that may need fixing."
    else
        log_success "All files are already valid!"
        exit 0
    fi
    
    # Step 2: Create backup (unless skipped)
    BACKUP_DIR=""
    if [[ "$SKIP_BACKUP" == "false" ]]; then
        log_info "💾 Step 2: Creating backup..."
        BACKUP_DIR=$(./scripts/backup-xhtml.sh)
        log_success "Backup created at $BACKUP_DIR"
    else
        log_warning "⚠️  Skipping backup creation (--skip-backup specified)"
    fi
    
    # Step 3: Run dry-run to show what would be fixed
    log_info "🔍 Step 3: Running dry-run to preview fixes..."
    if node scripts/fix-xhtml-safe.js --dry-run; then
        log_info "Dry run completed successfully."
    else
        log_warning "Dry run found issues that cannot be automatically fixed."
    fi
    
    # Step 4: Ask for confirmation to proceed (unless dry-run only)
    if [[ "$DRY_RUN" == "true" ]]; then
        log_info "🔍 Dry-run complete. No changes were made."
        exit 0
    fi
    
    if ! confirm_action "Do you want to proceed with applying the fixes?"; then
        log_info "Aborted by user. No changes were made."
        if [[ -n "$BACKUP_DIR" ]]; then
            log_info "Backup is available at: $BACKUP_DIR"
        fi
        exit 0
    fi
    
    # Step 5: Apply fixes
    log_info "🔧 Step 4: Applying fixes..."
    if node scripts/fix-xhtml-safe.js; then
        log_success "Fixes applied successfully!"
    else
        log_error "Some fixes could not be applied."
        if [[ -n "$BACKUP_DIR" ]]; then
            log_warning "You can restore from backup: cp $BACKUP_DIR/*.xhtml OEBPS/text/"
        fi
        exit 1
    fi
    
    # Step 6: Run validation again to confirm fixes
    log_info "🔍 Step 5: Running final validation..."
    if node scripts/validate-xhtml-safe.js; then
        log_success "🎉 All XHTML files are now valid!"
    else
        log_warning "Some issues remain. Check the validation output above."
    fi
    
    # Clean up old backups if successful (keep last 5)
    if [[ -d "backups" ]] && [[ "$SKIP_BACKUP" == "false" ]]; then
        log_info "🧹 Cleaning up old backups (keeping last 5)..."
        find backups -name "xhtml_*" -type d | sort | head -n -5 | xargs -r rm -rf
    fi
    
    log_success "✅ Safe XHTML workflow completed!"
}

main "$@"