#!/bin/bash

REPO_URL="https://github.com/TaliaGeo/ci-cd-sourceRepo.git"
CLONE_DIR="temprory-sourceRepo"

if [ -d "$CLONE_DIR" ]; then
  echo "Removing old clone directory..."
  rm -rf "$CLONE_DIR"
  sleep 2
fi


echo "Cloning repository..."
git clone "$REPO_URL" "$CLONE_DIR"
 
 python3 manage_inventory.py