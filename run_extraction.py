#!/usr/bin/env python3
"""
Game Mechanics Extraction System - Main Entry Point

This script runs the complete extraction pipeline to analyze and document
all game mechanics from decompiled code.

Usage:
    python run_extraction.py
    python run_extraction.py --config custom_config.yaml
    python run_extraction.py --mode single --system Combat
"""

from extraction_system.cli import main

if __name__ == '__main__':
    main()
