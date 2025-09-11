#!/bin/bash

# EPUB Validation Script
# This script validates the EPUB structure and content

set -e

echo "🔍 Starting EPUB validation..."

# Check if epubcheck is available
if ! command -v epubcheck &> /dev/null; then
    echo "⚠️  epubcheck not found. Installing via npm..."
    if command -v npm &> /dev/null; then
        npm install -g epubcheck
    else
        echo "❌ npm not found. Please install Node.js and npm first."
        echo "   Then run: npm install -g epubcheck"
        exit 1
    fi
fi

# Create temporary EPUB structure for validation
TEMP_DIR=$(mktemp -d)
EPUB_DIR="$TEMP_DIR/epub"
mkdir -p "$EPUB_DIR"

echo "📂 Creating EPUB structure in $EPUB_DIR..."

# Copy EPUB files to temp directory
mkdir -p "$EPUB_DIR/OEBPS"
mkdir -p "$EPUB_DIR/META-INF"

# Copy content files
cp *.xhtml "$EPUB_DIR/OEBPS/" 2>/dev/null || true
cp -r styles "$EPUB_DIR/OEBPS/" 2>/dev/null || true
cp -r images "$EPUB_DIR/OEBPS/" 2>/dev/null || true
cp content.opf "$EPUB_DIR/OEBPS/" 2>/dev/null || true

# Create mimetype file
echo "application/epub+zip" > "$EPUB_DIR/mimetype"

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
echo "📦 Creating EPUB package..."
zip -r0 epub.epub epub/mimetype
zip -r epub.epub epub/ -x epub/mimetype

# Validate the EPUB
echo "✅ Running epubcheck validation..."
if epubcheck epub.epub; then
    echo "🎉 EPUB validation passed!"
    VALIDATION_RESULT=0
else
    echo "❌ EPUB validation failed!"
    VALIDATION_RESULT=1
fi

# Cleanup
cd -
rm -rf "$TEMP_DIR"

# Additional HTML validation
echo "🔍 Running additional HTML validation..."

# Check for common EPUB issues
echo "  • Checking for missing alt attributes..."
MISSING_ALT=$(grep -r 'img.*src=' *.xhtml | grep -v 'alt=' || true)
if [ -n "$MISSING_ALT" ]; then
    echo "⚠️  Found images without alt attributes:"
    echo "$MISSING_ALT"
fi

echo "  • Checking for proper EPUB namespaces..."
MISSING_EPUB_NS=$(grep -L 'xmlns:epub="http://www.idpf.org/2007/ops"' *.xhtml || true)
if [ -n "$MISSING_EPUB_NS" ]; then
    echo "⚠️  Files missing EPUB namespace:"
    echo "$MISSING_EPUB_NS"
fi

echo "  • Checking for consistent DOCTYPE declarations..."
INCONSISTENT_DOCTYPE=$(grep -L '<!DOCTYPE html>' *.xhtml || true)
if [ -n "$INCONSISTENT_DOCTYPE" ]; then
    echo "⚠️  Files with inconsistent DOCTYPE:"
    echo "$INCONSISTENT_DOCTYPE"
fi

echo "✅ Additional validation checks completed."

exit $VALIDATION_RESULT