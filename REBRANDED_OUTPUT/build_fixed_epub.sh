cd /workspaces/Fm

# Stage all changes
git add .

# Commit with descriptive message
git commit -m "Fix EPUB: Standardize chapter quote pages and optimize digital publishing

✅ Fixed all 16 chapters to have single standalone image quote pages
✅ Removed duplicate quote-page sections from all chapters  
✅ Cleaned CSS manifest - removed problematic print-pod.css and print.css
✅ Enhanced worksheet and quiz layouts for digital reading
✅ Optimized responsive design for better device compatibility
✅ Maintained all chapter quote images (chapter-i through chapter-xvi)
✅ Ready for professional digital publishing distribution"

# Push to remote repository
git push origin main#!/bin/bash

# Build Fixed EPUB Script
# The Artisan's Path - Digital Publishing Optimized

cd /workspaces/Fm/REBRANDED_OUTPUT

echo "🔄 Building fixed EPUB..."

# Remove old fixed version if exists
rm -f dist/The-Artisans-Path-Fixed.epub

# Build EPUB with proper compression
zip -X -0 dist/The-Artisans-Path-Fixed.epub mimetype
zip -X -r dist/The-Artisans-Path-Fixed.epub META-INF content.opf
zip -X -r dist/The-Artisans-Path-Fixed.epub fonts images styles xhtml

echo "✅ Fixed EPUB created: dist/The-Artisans-Path-Fixed.epub"

# Show file size
if [ -f dist/The-Artisans-Path-Fixed.epub ]; then
    SIZE=$(ls -lh dist/The-Artisans-Path-Fixed.epub | awk '{print $5}')
    echo "📊 File size: $SIZE"
fi

echo "🔍 Fixed issues:"
echo "  ✅ Removed problematic print-pod.css from manifest"
echo "  ✅ Cleaned duplicate quiz/worksheet sections" 
echo "  ✅ Removed print.css references from XHTML files"
echo "  ✅ Optimized worksheet layouts for digital reading"
echo "  ✅ Improved quiz section formatting"
echo "  ✅ Enhanced responsive design for better device compatibility"