#!/bin/bash

# Install ffmpeg
apt-get update
apt-get install -y ffmpeg

# Start your bot
python3 main.py
