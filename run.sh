#!/bin/sh


image_name=$(basename $PWD)

docker run -d  --volume "${PWD}/data:/data" "${image_name}" python app.py app1 2
docker run -d  --volume "${PWD}/data:/data" "${image_name}" python app.py app2 7
