#!/bin/bash
echo "📦 Compiling EPUB..."

cd /workspace/Fm/output

# Create mimetype file
echo -n "application/epub+zip" > mimetype

# Create EPUB structure
zip -0Xq ../book.epub mimetype
zip -Xr9Dq ../book.epub META-INF OEBPS

echo "✅ EPUB compiled as book.epub"
