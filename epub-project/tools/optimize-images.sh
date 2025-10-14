#!/bin/bash
echo "🖼️  Optimizing images for EPUB..."

# Navigate to images directory
cd /workspace/Fm/output/OEBPS/images/

# Optimize JPEG files
echo "Optimizing JPEG files..."
find . -name "*.jpg" -o -name "*.jpeg" | while read file; do
    echo "Processing: $file"
    # Resize if larger than 1200px width, optimize to 85% quality
    mogrify -resize 1200x1200\> -quality 85 "$file"
    jpegoptim --size=150k "$file"
done

# Optimize PNG files
echo "Optimizing PNG files..."
find . -name "*.png" | while read file; do
    echo "Processing: $file"
    optipng -o7 "$file"
done

# Optimize SVG files
echo "Optimizing SVG files..."
find . -name "*.svg" | while read file; do
    echo "Processing: $file"
    svgo --multipass "$file"
done

echo "✅ Image optimization complete!"

# Display file sizes
echo "📊 Image file sizes:"
find . -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.svg" \) -exec ls -lh {} \;
