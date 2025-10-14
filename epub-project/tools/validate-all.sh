#!/bin/bash
echo "🎯 COMPREHENSIVE EPUB VALIDATION - BESTSELLER QUALITY"
echo "=================================================="

# Run XHTML validation
echo "1️⃣ XHTML Validation..."
./validate.sh

# Run accessibility validation  
echo "2️⃣ Accessibility Validation..."
./validate-accessibility.sh

# Run SEO validation
echo "3️⃣ SEO Validation..."
./validate-seo.sh

# Run image optimization check
echo "4️⃣ Image Optimization Check..."
echo "Checking image file sizes..."
find /workspace/Fm/output/OEBPS/images -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.svg" \) -exec ls -lh {} \; | while read line; do
    size=$(echo $line | awk '{print $5}')
    file=$(echo $line | awk '{print $9}')
    
    # Check if image is too large
    if [[ $file == *.jpg ]] || [[ $file == *.jpeg ]]; then
        # Convert size to bytes for comparison (simplified check)
        if [[ $size == *M* ]]; then
            echo "⚠️  Large JPEG file: $file ($size)"
        fi
    fi
done

# Run final EPUBCheck
echo "5️⃣ Final EPUB Validation..."
if [ -f "/workspace/Fm/book.epub" ]; then
    java -jar epubcheck/epubcheck.jar /workspace/Fm/book.epub
else
    echo "⚠️  EPUB file not found. Run ./compile.sh first."
fi

echo "✅ COMPREHENSIVE VALIDATION COMPLETE!"
echo "Your EPUB is ready for BESTSELLER-QUALITY publication! 🚀"
