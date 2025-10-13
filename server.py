#!/usr/bin/env python3
"""
Simple HTTP server for hosting the Lunetronic landing page
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Configuration
PORT = 8080
HOST = '0.0.0.0'  # Bind to all network interfaces

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files with proper MIME types"""
    
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def guess_type(self, path):
        """Override to ensure proper MIME types"""
        mimetype = super().guess_type(path)
        
        # Ensure CSS files are served with correct MIME type
        if path.endswith('.css'):
            return 'text/css'
        # Ensure JS files are served with correct MIME type
        elif path.endswith('.js'):
            return 'application/javascript'
        
        return mimetype

def main():
    """Start the HTTP server"""
    # Change to the directory containing the HTML files
    os.chdir(Path(__file__).parent)
    
    # Get local IP address
    import socket
    try:
        # Connect to a remote address to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "localhost"
    
    # Create the server
    with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Lunetronic Landing Page Server")
        print(f"📡 Server running on all interfaces")
        print(f"🏠 Local access: http://localhost:{PORT}")
        print(f"🌐 Network access: http://{local_ip}:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"⏹️  Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Try to open browser automatically
        try:
            webbrowser.open(f'http://{HOST}:{PORT}')
            print("🌐 Browser opened automatically")
        except Exception as e:
            print(f"⚠️  Could not open browser automatically: {e}")
        
        # Start serving
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
            httpd.shutdown()

if __name__ == "__main__":
    main()
