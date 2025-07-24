#!/bin/bash

REPO_URL="https://github.com/TaliaGeo/ci-cd-sourceRepo.git"
CLONE_DIR=" temprory-sourceRepo"

rm -rf "$CLONE_DIR"
git clone $REPO_URL
 
 python3 cicdpipeline.py