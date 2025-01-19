from kivy.uix.video import Video
from kivymd.uix.backdrop.backdrop import MDFloatLayout
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import requests
from kivy.lang import Builder
import cv2
import numpy as np


class VideoStream(Image):
    def __init__(self, url, **kwargs):
        super(VideoStream, self).__init__(**kwargs)
        self.url = url
        Clock.schedule_interval(self.update, 1.0 / 60)

    def update(self, dt):
        response = requests.get(self.url, stream=True)
        bytes_data = bytes()
        for chunk in response.iter_content(chunk_size=1024):
            bytes_data += chunk
            a = bytes_data.find(b'\xff\xd8')
            b = bytes_data.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes_data[a:b + 2]
                bytes_data = bytes_data[b + 2:]
                img = cv2.imdecode(np.frombuffer(jpg, np.uint8), cv2.IMREAD_COLOR)
                buffer = img.tobytes()
                texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
                texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
                self.texture = texture
                self.texture.flip_vertical()
                break

class MyApp(App):
    def build(self):
        return VideoStream(url='http://127.0.0.1:18231/video')

if __name__ == '__main__':
    MyApp().run()
