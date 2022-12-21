#/bin/bash

set -e

echo "Building subchart test deployment image as user: $USER"

cd $(dirname $0)

ROOT_DIR=$(git rev-parse --show-toplevel)

cd $ROOT_DIR
BRANCH_NAME=${BRANCH_NAME:-$(git rev-parse --abbrev-ref HEAD)}
IMAGE_NAME="erostamas/subchart_test"
echo "Image name is: $IMAGE_NAME, branch name is: $BRANCH_NAME"

cd $ROOT_DIR
docker build --no-cache -t "$IMAGE_NAME" -f $ROOT_DIR/subchart_test/env/deploymentenv/Dockerfile $ROOT_DIR/subchart_test/
docker login --username=erostamas --password 749af946-ad0c-4d57-ade7-dfcc06efb7e4 docker.io
docker push "$IMAGE_NAME":latest

echo "Done building playground rest service deployment image"
