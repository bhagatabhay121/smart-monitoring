from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.clock import Clock
import requests
from io import BytesIO
from PIL import Image as PILImage

KV = '''
BoxLayout:
    Image:
        id: video_stream
'''

class VideoStreamApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        Clock.schedule_interval(self.update_image, 1.0 / 30)  # Update at 30 FPS

    def update_image(self, dt):
        try:
            response = requests.get('https://youtu.be/CuFEaclhVcc?si=P2GlXkMAv5eBSLhY', stream=True)
            if response.status_code == 200:
                # Read the image data
                image_data = BytesIO(response.content)
                img = PILImage.open(image_data)
                img = img.transpose(PILImage.FLIP_TOP_BOTTOM)  # Flip if needed
                self.root.ids.video_stream.texture = self.texture_from_image(img)
        except Exception as e:
            print(f"Error: {e}")

    def texture_from_image(self, img):
        img = img.convert('RGBA')
        texture = self.texture_from_pil(img)
        return texture

    def texture_from_pil(self, img):
        texture = Image(texture_size=(img.width, img.height))
        texture.blit_buffer(img.tobytes(), colorfmt='rgba', bufferfmt='ubyte')
        return texture

if __name__ == '__main__':
    VideoStreamApp().run()