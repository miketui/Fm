#!/usr/bin/env python3
"""
Verify HOME directory EPUB structure
This script verifies that the HOME directory contains all necessary files
for EPUB compilation and follows EPUB standards.
"""
import os
from pathlib import Path

def verify_home_structure():
    """Verify the HOME directory structure"""
    print("🔍 Verifying HOME directory EPUB structure...\n")
    
    errors = []
    warnings = []
    
    # Check root level
    print("📁 Checking root level files...")
    if not os.path.exists('HOME/mimetype'):
        errors.append("Missing HOME/mimetype file")
    else:
        with open('HOME/mimetype', 'r') as f:
            mimetype = f.read().strip()
            if mimetype != 'application/epub+zip':
                errors.append(f"Invalid mimetype: {mimetype}")
            else:
                print("  ✅ mimetype is correct")
    
    # Check META-INF
    print("\n📁 Checking META-INF...")
    if not os.path.exists('HOME/META-INF/container.xml'):
        errors.append("Missing HOME/META-INF/container.xml")
    else:
        print("  ✅ container.xml exists")
    
    # Check OEBPS
    print("\n📁 Checking OEBPS...")
    if not os.path.exists('HOME/OEBPS/content.opf'):
        errors.append("Missing HOME/OEBPS/content.opf")
    else:
        print("  ✅ content.opf exists")
    
    # Check subdirectories
    subdirs = ['text', 'styles', 'fonts', 'images']
    for subdir in subdirs:
        path = f'HOME/OEBPS/{subdir}'
        if not os.path.exists(path):
            errors.append(f"Missing directory: {path}")
        else:
            file_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
            print(f"  ✅ {subdir}/ exists with {file_count} files")
    
    # Count XHTML files
    print("\n📄 Checking XHTML files...")
    text_dir = 'HOME/OEBPS/text'
    if os.path.exists(text_dir):
        xhtml_files = [f for f in os.listdir(text_dir) if f.endswith('.xhtml')]
        print(f"  ✅ Found {len(xhtml_files)} XHTML files")
        
        # Check for key files
        key_files = [
            '1-TitlePage.xhtml',
            'nav.xhtml',
            '9-chapter-i-unveiling-your-creative-odyssey.xhtml'
        ]
        for key_file in key_files:
            if key_file not in xhtml_files:
                errors.append(f"Missing key file: {key_file}")
            else:
                print(f"  ✅ {key_file} exists")
    
    # Count CSS files
    print("\n🎨 Checking CSS files...")
    styles_dir = 'HOME/OEBPS/styles'
    if os.path.exists(styles_dir):
        css_files = [f for f in os.listdir(styles_dir) if f.endswith('.css')]
        print(f"  ✅ Found {len(css_files)} CSS files")
        
        required_css = ['fonts.css', 'style.css', 'print.css']
        for css_file in required_css:
            if css_file not in css_files:
                errors.append(f"Missing CSS file: {css_file}")
            else:
                print(f"  ✅ {css_file} exists")
    
    # Count font files
    print("\n🔤 Checking font files...")
    fonts_dir = 'HOME/OEBPS/fonts'
    if os.path.exists(fonts_dir):
        font_files = [f for f in os.listdir(fonts_dir) if f.endswith('.woff2')]
        print(f"  ✅ Found {len(font_files)} font files")
    
    # Count image files
    print("\n🖼️  Checking image files...")
    images_dir = 'HOME/OEBPS/images'
    if os.path.exists(images_dir):
        image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpeg', '.jpg', '.svg', '.png'))]
        print(f"  ✅ Found {len(image_files)} image files")
    
    # Total file count
    print("\n📊 File count summary...")
    total_files = sum(1 for _, _, files in os.walk('HOME') for _ in files)
    print(f"  Total files in HOME: {total_files}")
    
    # Report results
    print("\n" + "="*60)
    if errors:
        print(f"❌ VALIDATION FAILED - {len(errors)} error(s) found:")
        for error in errors:
            print(f"  • {error}")
    else:
        print("✅ ALL CHECKS PASSED!")
        print("\nHOME directory is ready for EPUB compilation.")
        print("\nTo build EPUB, run:")
        print("  python3 build_home_epub.py")
    
    if warnings:
        print(f"\n⚠️  {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  • {warning}")
    
    return len(errors) == 0

if __name__ == "__main__":
    success = verify_home_structure()
    exit(0 if success else 1)
