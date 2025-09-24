#!/usr/bin/env python3
import zipfile
import os
from pathlib import Path

def create_epub():
    epub_path = './dist/curls-and-contemplation.epub'

    # Ensure dist directory exists
    os.makedirs('dist', exist_ok=True)

    print("🔄 Creating updated EPUB with fixed formatting...")

    with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Add mimetype first (uncompressed)
        print("📄 Adding mimetype...")
        epub.write('mimetype', compress_type=zipfile.ZIP_STORED)

        # Add META-INF
        print("📁 Adding META-INF...")
        for root, dirs, files in os.walk('META-INF'):
            for file in files:
                file_path = os.path.join(root, file)
                epub.write(file_path)

        # Add OEBPS
        print("📚 Adding OEBPS...")
        for root, dirs, files in os.walk('OEBPS'):
            for file in files:
                file_path = os.path.join(root, file)
                epub.write(file_path)

    print(f"✅ EPUB created successfully: {epub_path}")

    # Show file size
    file_size = os.path.getsize(epub_path) / (1024*1024)
    print(f"📊 File size: {file_size:.2f} MB")

    return epub_path

if __name__ == "__main__":
    create_epub()