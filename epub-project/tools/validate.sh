#!/bin/bash
echo "🔍 Validating EPUB structure..."

# Validate XHTML files
echo "Validating XHTML files..."
for file in /workspace/Fm/output/OEBPS/text/*.xhtml; do
    echo "Checking: $file"
    java -jar ../tools/vnu.jar "$file"
done

# Validate EPUB package
echo "Validating complete EPUB..."
java -jar tools/epubcheck/epubcheck.jar /workspace/Fm/output/book.epub

echo "✅ Validation complete!"
