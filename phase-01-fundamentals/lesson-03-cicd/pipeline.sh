#!/bin/bash
set -e

echo "=== Stage 1: Install dependencies ==="
pip install -r requirements.txt --quiet

echo "=== Stage 2: Run tests ==="
python3 -m pytest -v

echo "=== Stage 3: Build artifact ==="
VERSION=$(git rev-parse --short HEAD)
mkdir -p dist
tar -czf dist/app-$VERSION.tar.gz app.py requirements.txt

echo "=== Pipeline succeeded: dist/app-$VERSION.tar.gz ==="
