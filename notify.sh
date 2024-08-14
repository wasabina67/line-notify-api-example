#!/bin/bash

source .env

MESSAGE="message"
IMAGE_FILE="./images/sample.jpg"
URL="https://notify-api.line.me/api/notify"

curl -X POST -H "Authorization: Bearer $ACCESS_TOKEN" \
    -F "message=$MESSAGE" \
    -F "imageFile=@$IMAGE_FILE" \
    $URL
