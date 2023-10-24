#!/bin/sh

cur_dir='/home/wines-nuc8/sakthi/sierra-video-streaming'
# Stream video from camera
python3 $cur_dir/ffmpeg_run.py

sleep 5

# Set camera exposure suitable for outdoors.
v4l2-ctl -c exposure_auto=1
v4l2-ctl -c exposure_absolute=1
v4l2-ctl -c gain=10
v4l2-ctl -c brightness=100
v4l2-ctl -c backlight_compensation=1
