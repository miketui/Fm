#!/bin/bash

# XHTML Backup Script
# Creates timestamped backups of all XHTML files before processing

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

# Generate timestamp for backup directory
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="backups/xhtml_${TIMESTAMP}"

main() {
    log_info "🔄 Creating XHTML backups..."
    
    # Check if OEBPS/text directory exists
    if [[ ! -d "OEBPS/text" ]]; then
        log_error "OEBPS/text directory not found. Run from EPUB project root."
        exit 1
    fi
    
    # Create backup directory
    mkdir -p "$BACKUP_DIR"
    
    # Copy all XHTML files
    local count=0
    while IFS= read -r -d '' file; do
        cp "$file" "$BACKUP_DIR/"
        count=$((count + 1))
    done < <(find OEBPS/text -name "*.xhtml" -print0)
    
    # Create metadata file
    cat > "$BACKUP_DIR/backup_info.txt" << EOF
XHTML Backup Information
========================
Created: $(date)
Files backed up: $count
Original location: $(pwd)/OEBPS/text/
Backup location: $(pwd)/$BACKUP_DIR/

To restore all files:
cp $BACKUP_DIR/*.xhtml OEBPS/text/

To restore individual file:
cp $BACKUP_DIR/filename.xhtml OEBPS/text/filename.xhtml
EOF
    
    log_success "✅ Backup created: $BACKUP_DIR"
    log_info "📊 Backed up $count XHTML files"
    log_info "ℹ️  Backup info saved to $BACKUP_DIR/backup_info.txt"
    
    echo "$BACKUP_DIR"  # Return backup directory for scripts to use
}

main "$@"