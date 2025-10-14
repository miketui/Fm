#!/bin/bash
echo "📂 Extracting EPUB for editing..."

if [ -z "$1" ]; then
    echo "Usage: ./unzip-epub.sh <epub-file>"
    exit 1
fi

EPUB_FILE="$1"
EXTRACT_DIR="/workspace/Fm/epub-project/input"

# Extract EPUB
unzip -q "$EPUB_FILE" -d "$EXTRACT_DIR"

echo "✅ EPUB extracted to $EXTRACT_DIR/"
echo "Files structure:"
find "$EXTRACT_DIR" -type f | head -20
