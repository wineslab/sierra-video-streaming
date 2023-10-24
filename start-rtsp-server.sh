#!/bin/sh

# It is sufficient to run this scirpt once.

# Start RTSP server in docker container.
docker run -d --restart always --network=host bluenviron/mediamtx:latest

# Start the server container on system boot
sudo systemctl enable docker

# Start the container now
sudo systemctl start docker
