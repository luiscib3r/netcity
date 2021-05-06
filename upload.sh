#!/bin/bash

ID=$(curl -X 'POST' \
  'http://localhost:8000/api/v1/attachments/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H 'API_KEY: SECRET' \
  -F 'file=@app/main.py')

echo $ID

curl -X 'POST' \
  'http://localhost:8000/api/v1/app_release/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'API_KEY: SECRET' \
  -d '{
  "name": "EDV Cli",
  "version": "1.0.6",
  "description": "",
  "apps": [
    '"$ID"' 
  ]
}'