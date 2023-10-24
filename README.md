# sierra-video-streaming
All setting required to stream video from a webcam attached to a linux box.

## Steps
1. Start the RTSP server with `./start-rtsp-server.sh`. It runs in a docker container which starts upon every reboot.
2. Start the video stream with `./start-video.sh`. This script pulls raw video from the camera, performs H264 hardware encoding and pushes it to the RTSP server. Fell free to change the parameters based on the camera used.
3. On the receiving side, the stream can be viewed using `VLC` or `ffplay`. The RTSP URL should be `rtsp://<IP of the server>:8554/mystream`.
