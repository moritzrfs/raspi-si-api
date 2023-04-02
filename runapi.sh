#!/bin/bash

# Activate Python environment
source /home/pi/repos/raspi-si-api/env/bin/activate

# Start Uvicorn server
cd /home/pi/repos/raspi-si-api
uvicorn main:app --reload --host 0.0.0.0 --port 8080