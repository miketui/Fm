import os
import re
from pathlib import Path

BASE_DIR = Path('/root/repo/REBRANDED-output/xhtml')
IMAGE_DIR = Path('/root/repo/REBRANDED-output/images')

QUOTE_TEMPLATE = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Quote</title>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
  <style>
    .quote-page {{
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 90vh;
        padding: 20px;
        page-break-inside: avoid;
    }}
    .quote-page img {{
        max-width: 100%;
        max-height: 85vh;
        object-fit: contain;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-radius: 0.5rem;
    }}
    body {{ margin: 0; padding: 0; }}
  </style>
</head>
<body class="quote-body">
<section class="quote-page">
<figure>
<img src="../images/{img_filename}" alt="Inspirational quote" />
</figure>
</section>
</body>
</html>
'''

def process_chapters():
    files = sorted(list(BASE_DIR.glob('*.xhtml')))
    
    for file_path in files:
        print(f"Checking {file_path.name}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for inline quote section
        match = re.search(r'(<section class="quote-page">.*?</section>)', content, re.DOTALL)
        
        if match:
            print(f"  Found quote section in {file_path.name}. Extracting...")
            quote_content = match.group(1)
            
            # Extract image filename from the quote content
            img_match = re.search(r'src="../images/([^\"]+)"', quote_content)
            if img_match:
                img_filename = img_match.group(1)
            else:
                print(f"  WARNING: No image found in quote section of {file_path.name}")
                continue
                
            # Create new quote file
            new_filename = file_path.stem + '-quote.xhtml'
            new_file_path = BASE_DIR / new_filename
            
            new_xhtml = QUOTE_TEMPLATE.format(img_filename=img_filename)
            
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(new_xhtml)
            print(f"  Created {new_filename}")
            
            # Remove section from original file
            # Also remove any preceding page break if it exists and is now redundant
            # The pattern in create_chapters.py was:
            # </section>\n\n<section class="quote-page">...
            # We just remove the quote section.
            
            new_content = content.replace(quote_content, '')
            
            # Cleanup trailing/double newlines or page breaks if necessary
            # For now, just removing the section is safe.
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  Updated {file_path.name}")
            
        # Special handling for Preface and Conclusion if they don't have inline quotes
        elif 'Preface.xhtml' in file_path.name:
            # Check if quote file already exists
            quote_file = BASE_DIR / '7-Preface-quote.xhtml'
            if not quote_file.exists():
                print("  Creating separate quote file for Preface...")
                new_xhtml = QUOTE_TEMPLATE.format(img_filename='preface-quote.jpeg')
                with open(quote_file, 'w', encoding='utf-8') as f:
                    f.write(new_xhtml)
                print(f"  Created {quote_file.name}")
                
        elif 'Conclusion.xhtml' in file_path.name:
             # Check if quote file already exists
            quote_file = BASE_DIR / '28-Conclusion-quote.xhtml'
            if not quote_file.exists():
                print("  Creating separate quote file for Conclusion...")
                new_xhtml = QUOTE_TEMPLATE.format(img_filename='conclusion-quote.jpeg')
                with open(quote_file, 'w', encoding='utf-8') as f:
                    f.write(new_xhtml)
                print(f"  Created {quote_file.name}")

if __name__ == '__main__':
    process_chapters()
