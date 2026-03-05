#!/usr/bin/env python3
"""
DCM Pfsense APT Manager - Web Interface Entry Point

This is the main entry point for the web interface.
"""

import sys
import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from dcm_pfsense_apt_manager.web.app import app

# Support Docker environment variable for data directory
DATA_DIR = os.getenv('DCM_DATA_DIR', str(Path.home() / '.dcm-apt-manager'))
DEFAULT_CONFIG_DIR = Path(DATA_DIR)

if __name__ == '__main__':
    # Ensure config directory exists
    DEFAULT_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("DCM Pfsense APT Manager - Web Interface")
    print("=" * 60)
    print(f"\n🌐 Starting web server on http://0.0.0.0:5000")
    print(f"📁 Configuration directory: {DEFAULT_CONFIG_DIR}")
    print(f"\n🔐 Default credentials:")
    print(f"   Username: admin")
    print(f"   Password: admin")
    print(f"\n⚠️  Change the default password in production!")
    print(f"\n💡 Press Ctrl+C to stop the server\n")
    print("=" * 60 + "\n")
    
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down gracefully...")
        sys.exit(0)
