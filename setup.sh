#!/bin/bash

# EPUB Codex Setup Script
# Unveiling Your Creative Odyssey - ACISS Design Implementation

echo "🚀 Setting up Codex environment for EPUB project..."

PROJECT_ROOT="/workspace/Fm"
CANONICAL_INPUT_DIR="$PROJECT_ROOT/OEBPS/text"
CANONICAL_OUTPUT_DIR="$PROJECT_ROOT/output/OEBPS/text"
CANONICAL_OUTPUT_IMAGES_DIR="$PROJECT_ROOT/output/OEBPS/images"
CANONICAL_OUTPUT_ROOT="$PROJECT_ROOT/output"

# Create project directory structure
echo "📁 Creating project structure..."
mkdir -p epub-project/{input,output,backups,validation,tools}
mkdir -p epub-project/input/{OEBPS/text,OEBPS/styles,OEBPS/images,META-INF}
mkdir -p epub-project/output/{OEBPS/text,OEBPS/styles,OEBPS/images,META-INF}
mkdir -p "$CANONICAL_INPUT_DIR" "$CANONICAL_OUTPUT_DIR" "$CANONICAL_OUTPUT_IMAGES_DIR" "$CANONICAL_OUTPUT_ROOT"

# Install required tools for BESTSELLER QUALITY
echo "🛠️  Installing dependencies for professional publishing..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Installing Node.js..."
    curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# Install image optimization tools
echo "🖼️  Installing image optimization tools..."
sudo apt-get update
sudo apt-get install -y jpegoptim optipng imagemagick

# Install SVGO for SVG optimization
npm install -g svgo

# Install EPUBCheck
echo "📚 Installing EPUBCheck..."
wget https://github.com/w3c/epubcheck/releases/download/v5.0.0/epubcheck-5.0.0.zip
unzip epubcheck-5.0.0.zip
mv epubcheck-5.0.0 epub-project/tools/epubcheck
rm epubcheck-5.0.0.zip

# Install HTML validator
npm install -g vnu-jar

# Install EPUB creation tools
npm install -g epub-gen-memory

# Create image optimization script
cat > epub-project/tools/optimize-images.sh << 'EOF'
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
EOF

chmod +x epub-project/tools/optimize-images.sh

# Create accessibility validation script
cat > epub-project/tools/validate-accessibility.sh << 'EOF'
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
EOF

chmod +x epub-project/tools/validate-accessibility.sh

# Create SEO metadata validator
cat > epub-project/tools/validate-seo.sh << 'EOF'
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
EOF

chmod +x epub-project/tools/validate-seo.sh

# Create comprehensive validation script
cat > epub-project/tools/validate-all.sh << 'EOF'
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
EOF

chmod +x epub-project/tools/validate-all.sh

# Create validation script
cat > epub-project/tools/validate.sh << 'EOF'
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
EOF

chmod +x epub-project/tools/validate.sh

# Create EPUB compilation script
cat > epub-project/tools/compile.sh << 'EOF'
#!/bin/bash
echo "📦 Compiling EPUB..."

cd /workspace/Fm/output

# Create mimetype file
echo -n "application/epub+zip" > mimetype

# Create EPUB structure
zip -0Xq ../book.epub mimetype
zip -Xr9Dq ../book.epub META-INF OEBPS

echo "✅ EPUB compiled as book.epub"
EOF

chmod +x epub-project/tools/compile.sh

# Create unzip script for existing EPUB
cat > epub-project/tools/unzip-epub.sh << 'EOF'
#!/bin/bash
echo "📂 Extracting EPUB for editing..."

if [ -z "$1" ]; then
    echo "Usage: ./unzip-epub.sh <epub-file>"
    exit 1
fi

EPUB_FILE="$1"
EXTRACT_DIR="input"

# Extract EPUB
unzip -q "$EPUB_FILE" -d "$EXTRACT_DIR"

echo "✅ EPUB extracted to $EXTRACT_DIR/"
echo "Files structure:"
find "$EXTRACT_DIR" -type f | head -20
EOF

chmod +x epub-project/tools/unzip-epub.sh

# Create file checker script
cat > epub-project/tools/check-files.sh << 'EOF'
#!/bin/bash
echo "📋 Checking EPUB file structure..."

INPUT_DIR="/workspace/Fm/OEBPS/text"
EXPECTED_FILES=45

if [ ! -d "$INPUT_DIR" ]; then
    echo "❌ Input directory not found: $INPUT_DIR"
    exit 1
fi

ACTUAL_FILES=$(find "$INPUT_DIR" -name "*.xhtml" | wc -l)

echo "Expected files: $EXPECTED_FILES"
echo "Actual files: $ACTUAL_FILES"

if [ "$ACTUAL_FILES" -eq "$EXPECTED_FILES" ]; then
    echo "✅ File count matches!"
else
    echo "⚠️  File count mismatch!"
fi

echo "📝 File listing:"
find "$INPUT_DIR" -name "*.xhtml" | sort
EOF

chmod +x epub-project/tools/check-files.sh

echo "✅ Codex setup complete!"
echo ""
echo "📁 Project structure created in: epub-project/"
echo "🛠️  Tools installed in: epub-project/tools/"
echo ""
echo "Next steps:"
echo "1. Place your EPUB file in epub-project/"
echo "2. Run: ./tools/unzip-epub.sh your-book.epub"
echo "3. Run codex with the AGENTS.md instructions"
echo "4. Use ./tools/validate.sh to check output"
echo "5. Use ./tools/compile.sh to create final EPUB"