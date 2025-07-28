#!/bin/bash
CONTAINER_NAME="inventory-container"
IMAGE_NAME="restaurant-inventory-pipeline-image"  
VERSION_TAG=$(docker images --format "{{.Tag}}" "$IMAGE_NAME" | grep -v latest | head -n 1)
if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing existing container..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
else
    echo "No existing container found."
fi

echo "Deploying container from image version: $VERSION_TAG ..."
docker run -d --name $CONTAINER_NAME -p 8080:8080 "$IMAGE_NAME:$VERSION_TAG"

