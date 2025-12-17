#!/usr/bin/env python3
"""
Build final EPUB with error fixes
"""
import os
import zipfile
import sys

def build_epub():
    """Build the final EPUB file"""
    
    # Change to REBRANDED_OUTPUT directory
    output_dir = "/workspaces/Fm/REBRANDED_OUTPUT"
    os.chdir(output_dir)
    
    epub_name = "The-Artisans-Path.epub"
    
    # Remove existing EPUB if it exists
    if os.path.exists(epub_name):
        os.remove(epub_name)
    
    # Create EPUB zip file
    with zipfile.ZipFile(epub_name, 'w', zipfile.ZIP_STORED) as epub:
        # Add mimetype first (uncompressed)
        if os.path.exists('mimetype'):
            epub.write('mimetype', 'mimetype')
        
        # Add META-INF
        if os.path.exists('META-INF'):
            for root, dirs, files in os.walk('META-INF'):
                for file in files:
                    file_path = os.path.join(root, file)
                    epub.write(file_path, file_path)
        
        # Add content.opf
        if os.path.exists('content.opf'):
            epub.write('content.opf', 'content.opf')
        
        # Add XHTML files
        if os.path.exists('xhtml'):
            for root, dirs, files in os.walk('xhtml'):
                for file in files:
                    if file.endswith('.xhtml'):
                        file_path = os.path.join(root, file)
                        epub.write(file_path, file_path)
        
        # Add images
        if os.path.exists('images'):
            for root, dirs, files in os.walk('images'):
                for file in files:
                    file_path = os.path.join(root, file)
                    epub.write(file_path, file_path)
        
        # Add fonts
        if os.path.exists('fonts'):
            for root, dirs, files in os.walk('fonts'):
                for file in files:
                    file_path = os.path.join(root, file)
                    epub.write(file_path, file_path)
        
        # Add styles
        if os.path.exists('styles'):
            for root, dirs, files in os.walk('styles'):
                for file in files:
                    if file.endswith('.css'):
                        file_path = os.path.join(root, file)
                        epub.write(file_path, file_path)
    
    print(f"✅ EPUB created successfully: {epub_name}")
    
    # Check file size
    file_size = os.path.getsize(epub_name)
    print(f"📏 File size: {file_size / (1024*1024):.2f} MB")
    
    return epub_name

if __name__ == "__main__":
    try:
        epub_path = build_epub()
        print(f"\n🎉 EPUB build complete!")
        print(f"📍 Location: /workspaces/Fm/REBRANDED_OUTPUT/{epub_path}")
    except Exception as e:
        print(f"❌ Error building EPUB: {e}")
        sys.exit(1)