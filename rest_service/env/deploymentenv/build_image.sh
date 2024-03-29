#/bin/bash

set -e

echo "Building playground rest service deployment image as user: $USER"

echo "Environment variables:"
env

cd $(dirname $0)

ROOT_DIR=$(git rev-parse --show-toplevel)

SUCCESS=0

cd $ROOT_DIR
BRANCH_NAME=${BRANCH_NAME:-$(git rev-parse --abbrev-ref HEAD)}
IMAGE_NAME="erostamas/playground_rest_service_${BRANCH_NAME}"
echo "Image name is: $IMAGE_NAME, branch name is: $BRANCH_NAME"

cd $ROOT_DIR
docker build -t "$IMAGE_NAME" -f $ROOT_DIR/rest_service/env/deploymentenv/Dockerfile $ROOT_DIR/rest_service/
docker login --username=erostamas --password 749af946-ad0c-4d57-ade7-dfcc06efb7e4 docker.io
docker push "$IMAGE_NAME":latest

SUCCESS=$?
echo "Done building playground rest service deployment image"
