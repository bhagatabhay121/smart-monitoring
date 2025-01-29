from flask import Flask, Response
import cv2
import time
import numpy as np
import pygetwindow as gw
import pyautogui
app = Flask(__name__)


def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return frame

def generate_frames():
    while True:
        frame = capture_screen()
        #frame = cv2.resize(frame, (640, 360))  # Resize to a smaller resolution
        _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])  # Lower JPEG quality
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.03)

@app.route('/video')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=18231, debug=True)
