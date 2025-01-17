import subprocess


#for linux : ffmpeg -f x11grab -i :0.0 -f mpegts http://localhost:8080



def stream_screen(stream_url):
    # FFmpeg command to capture the screen and stream it
    command = [
        'ffmpeg',
        '-f', 'gdigrab',          # Input format
        '-framerate', '30',       # Frame rate
        '-i', 'desktop',          # Input source (desktop)
        '-f', 'flv',              # Output format
        stream_url                # Output URL
    ]

    # Start the FFmpeg process
    process = subprocess.Popen(command)
    return process

if __name__ == "__main__":
    # Replace with your actual streaming URL
    stream_url = 'rtmp://127.0.0.1:4040'
    process = stream_screen(stream_url)

    try:
        # Keep the script running while streaming
        print("Streaming... Press Ctrl+C to stop.")
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping the stream...")
        process.terminate()
        process.wait()
        print("Stream stopped.")