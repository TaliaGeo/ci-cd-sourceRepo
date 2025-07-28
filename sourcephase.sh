#!/bin/bash
REPO_URL="https://github.com/TaliaGeo/ci-cd-sourceRepo.git"
CLONE_DIR="temprory-sourceRepo"

echo "Removing old clone directory..."
rm -rf "$CLONE_DIR"

echo "Cloning repository..."
git clone "$REPO_URL" "$CLONE_DIR"
echo "Clone successful: $(pwd)/$CLONE_DIR"
