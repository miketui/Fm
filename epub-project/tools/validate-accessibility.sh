#!/bin/bash
echo "♿ Validating accessibility features..."

ERRORS=0
WARNINGS=0

echo "Checking for alt text on images..."
find /workspace/Fm/output/OEBPS/text -name "*.xhtml" -exec grep -l '<img' {} \; | while read file; do
    # Check for images without alt text
    if grep -q '<img[^>]*src[^>]*>' "$file" && ! grep -q 'alt=' "$file"; then
        echo "❌ Missing alt text in: $file"
        ((ERRORS++))
    fi
    
    # Check for empty alt text on content images
    if grep -q 'alt=""' "$file" && ! grep -q 'brushstroke\|ornament\|decorative' "$file"; then
        echo "⚠️  Empty alt text may be inappropriate in: $file"
        ((WARNINGS++))
    fi
done

echo "Checking heading hierarchy..."
find /workspace/Fm/output/OEBPS/text -name "*.xhtml" -exec grep -l '<h[1-6]' {} \; | while read file; do
    # Extract heading levels and check sequence
    grep -o '<h[1-6]' "$file" | sed 's/<h//' | sort -n | uniq -c
done

echo "Checking for ARIA labels..."
ARIA_COUNT=$(find /workspace/Fm/output/OEBPS/text -name "*.xhtml" -exec grep -c 'aria-\|role=' {} \; | awk '{sum+=$1} END {print sum}')
echo "Found $ARIA_COUNT ARIA attributes across all files"

echo "Checking for semantic markup..."
SEMANTIC_COUNT=$(find /workspace/Fm/output/OEBPS/text -name "*.xhtml" -exec grep -c '<nav\|<main\|<section\|<article\|<aside\|<figure' {} \; | awk '{sum+=$1} END {print sum}')
echo "Found $SEMANTIC_COUNT semantic HTML elements"

echo "✅ Accessibility validation complete!"
echo "Errors: $ERRORS, Warnings: $WARNINGS"
