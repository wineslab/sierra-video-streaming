import sys
import subprocess
import time

def run():
    # Receive video stream from USB camera /dev/video0 in raw format (nv12). Encode it to H264 using Intel's hardware accelerator. Send to RTSP server running in docker container.
    command = "ffmpeg -re -input_format nv12 -video_size 1920x1080 -framerate 30 -i /dev/video0 -vaapi_device /dev/dri/renderD128 -vf format=nv12,hwupload -vcodec h264_vaapi -qp 18 -f rtsp -rtsp_transport tcp rtsp://localhost:8554/mystream".split()

    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print("stdout:", out.decode())
    print("stderr:", err.decode())
    return process

if __name__ == '__main__':
    process = run()

    while True:
        if process.poll() is not None:
            print('FFmpeg process ended. Restarting it.')
            process = run()
        time.sleep(5)
