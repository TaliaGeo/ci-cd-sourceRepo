#!/bin/bash
echo "starting build phase..."
IMAGE_NAME="restaurant-inventory-pipeline-image"
docker build -t "$IMAGE_NAME" .
echo "Build phase completed successfully."