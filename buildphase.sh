#!/bin/bash
echo "starting build phase..."
IMAGE_NAME="restaurant-inventory-pipeline-image"
VERSION_TAG=$(date +%Y%m%d-%H%M)
docker build -t "$IMAGE_NAME:$VERSION_TAG" .
docker tag $IMAGE_NAME:$VERSION_TAG $IMAGE_NAME:latest
echo "Built $IMAGE_NAME with version: $VERSION"
