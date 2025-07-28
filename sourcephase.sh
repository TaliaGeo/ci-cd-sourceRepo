#!/bin/bash
set -e
REPO_URL="https://github.com/TaliaGeo/ci-cd-sourceRepo.git"
CLONE_DIR="temprory-sourceRepo"

echo " Current directory: $PWD"
if [ -d "$CLONE_DIR" ]; then
  echo "Removing old clone directory..."
  rm -rf "$CLONE_DIR"
fi


echo "Cloning repository..."
if git clone "$REPO_URL" "$CLONE_DIR"; then
  echo "Clone successful"
else
  echo "Clone failed"
  exit 1
fi
cd "$CLONE_DIR" || exit 1
pwd
