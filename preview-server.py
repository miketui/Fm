#!/usr/bin/env python3
"""
Simple HTTP server for previewing XHTML files with proper MIME types.
Serves the EPUB content directory with correct content types.
"""

import http.server
import socketserver
import os
import sys
from urllib.parse import unquote

PORT = 8000

class XHTMLHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler that serves XHTML files with proper MIME types."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def guess_type(self, path):
        """Override to set correct MIME type for XHTML files."""
        mimetype = super().guess_type(path)
        
        # Set proper MIME type for XHTML files
        if path.endswith('.xhtml'):
            return 'application/xhtml+xml'
        
        return mimetype
    
    def end_headers(self):
        """Add CORS headers to allow local file access."""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom log format."""
        sys.stdout.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format % args))

def main():
    """Start the preview server."""
    try:
        with socketserver.TCPServer(("", PORT), XHTMLHandler) as httpd:
            print("=" * 70)
            print("🌐 XHTML Preview Server Running")
            print("=" * 70)
            print(f"📂 Serving directory: {os.getcwd()}")
            print(f"🔗 Server URL: http://localhost:{PORT}")
            print(f"📄 Preview URL: http://localhost:{PORT}/xhtml-preview.html")
            print("=" * 70)
            print("\n📋 Quick Links:")
            print(f"   • Title Page: http://localhost:{PORT}/xhtml-preview.html?file=OEBPS/text/1-TitlePage.xhtml")
            print(f"   • Table of Contents: http://localhost:{PORT}/xhtml-preview.html?file=OEBPS/text/3-TableOfContents.xhtml")
            print(f"   • Navigation: http://localhost:{PORT}/xhtml-preview.html?file=OEBPS/text/nav.xhtml")
            print("\n💡 Usage:")
            print("   1. Open the preview URL in your browser")
            print("   2. Select any XHTML file from the dropdown")
            print("   3. The file will be displayed with proper styling")
            print("\n⏹️  Press Ctrl+C to stop the server\n")
            print("=" * 70)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"\n❌ Error: Port {PORT} is already in use.")
            print(f"   Try closing other applications or use a different port.\n")
            sys.exit(1)
        else:
            raise

if __name__ == "__main__":
    main()
