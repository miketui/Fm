#!/usr/bin/env python3
"""
Build EPUB from HOME directory
This script creates an EPUB file from the HOME directory structure
"""
import zipfile
import os
from pathlib import Path

def create_epub_from_home():
    """Create EPUB from HOME directory"""
    epub_path = './dist/home-curls-and-contemplation.epub'
    
    # Ensure dist directory exists
    os.makedirs('dist', exist_ok=True)
    
    print("🔄 Creating EPUB from HOME directory...")
    
    with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Add mimetype first (uncompressed, no compression)
        print("📄 Adding mimetype...")
        epub.write('HOME/mimetype', arcname='mimetype', compress_type=zipfile.ZIP_STORED)
        
        # Add META-INF
        print("📁 Adding META-INF...")
        for root, dirs, files in os.walk('HOME/META-INF'):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = file_path.replace('HOME/', '')
                epub.write(file_path, arcname=arcname)
        
        # Add OEBPS
        print("📚 Adding OEBPS...")
        for root, dirs, files in os.walk('HOME/OEBPS'):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = file_path.replace('HOME/', '')
                epub.write(file_path, arcname=arcname)
    
    print(f"✅ EPUB created successfully: {epub_path}")
    
    # Show file size
    file_size = os.path.getsize(epub_path) / (1024*1024)
    print(f"📊 File size: {file_size:.2f} MB")
    
    # Show file count
    file_count = sum(1 for _, _, files in os.walk('HOME') for _ in files)
    print(f"📋 Total files: {file_count}")
    
    return epub_path

if __name__ == "__main__":
    create_epub_from_home()
