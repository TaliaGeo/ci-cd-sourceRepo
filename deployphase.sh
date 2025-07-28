#!/bin/bash
CONTAINER_NAME="inventory-container"
IMAGE_NAME="restaurant-inventory-pipeline-image"  


if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing existing container..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
else
    echo "No existing container found."
fi

echo "Deploying container from image: $IMAGE_NAME:latest ..."
docker run -d --name $CONTAINER_NAME -p 8080:8080 "$IMAGE_NAME:latest"

