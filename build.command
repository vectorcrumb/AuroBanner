#!/bin/bash
cd -- "$(dirname "$BASH_SOURCE")"
pyinstaller --onefile --icon UCcolor.icns --name AuroBanner main.py