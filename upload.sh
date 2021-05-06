#!/bin/bash

curl -X 'POST' \
  'http://localhost:8000/api/v1/attachments/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H 'API_KEY: SECRET' \
  -F 'file=@app/main.py'