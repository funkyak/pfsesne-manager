#!/usr/bin/env python3
"""
DCM Pfsense APT Manager - Main CLI Entry Point

This is the main entry point for the command-line interface.
"""

import sys
from dcm_pfsense_apt_manager.cli.main import cli

if __name__ == '__main__':
    sys.exit(cli())
