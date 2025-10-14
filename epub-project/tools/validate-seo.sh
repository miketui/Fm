#!/bin/bash
echo "🔍 Validating SEO metadata..."

PACKAGE_FILE="/workspace/Fm/output/OEBPS/package.opf"

if [ ! -f "$PACKAGE_FILE" ]; then
    echo "❌ package.opf not found!"
    exit 1
fi

echo "Checking required metadata..."

# Check for enhanced title
if grep -q '<dc:title>.*:.*</dc:title>' "$PACKAGE_FILE"; then
    echo "✅ Enhanced title with subtitle found"
else
    echo "❌ Missing enhanced title with subtitle"
fi

# Check for detailed description
DESC_LENGTH=$(grep -o '<dc:description>.*</dc:description>' "$PACKAGE_FILE" | wc -c)
if [ "$DESC_LENGTH" -gt 500 ]; then
    echo "✅ Detailed description found ($DESC_LENGTH characters)"
else
    echo "❌ Description too short ($DESC_LENGTH characters)"
fi

# Check for multiple subject tags
SUBJECT_COUNT=$(grep -c '<dc:subject>' "$PACKAGE_FILE")
if [ "$SUBJECT_COUNT" -gt 5 ]; then
    echo "✅ Multiple subject tags found ($SUBJECT_COUNT)"
else
    echo "❌ Need more subject tags (found $SUBJECT_COUNT, need >5)"
fi

# Check for accessibility metadata
if grep -q 'schema:accessibility' "$PACKAGE_FILE"; then
    echo "✅ Accessibility metadata found"
else
    echo "❌ Missing accessibility metadata"
fi

echo "✅ SEO validation complete!"
