#!/bin/bash
docker rm -f web_cybercore
docker build -t web_cybercore . && \
docker run --name=web_cybercore --rm -p1337:1337 -it web_cybercore