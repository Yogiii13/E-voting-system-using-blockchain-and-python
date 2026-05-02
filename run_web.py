#!/usr/bin/env python3
import sys
import subprocess

try:
    import flask
except ImportError:
    print("Installing Flask...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Flask==2.3.3"])

from e_voting.app import app

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🔐 Secure Blockchain Voting System")
    print("="*60)
    print("\n✅ Server starting on http://localhost:5000")
    print("   Open your browser and navigate to: http://localhost:5000\n")
    print("Press Ctrl+C to stop the server\n")
    
    app.run(debug=False, host='0.0.0.0', port=5000)
