from kivy.uix.accordion import ListProperty
from kivymd.uix.behaviors import HoverBehavior
from kivy.uix.textinput import Texture
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from firebase import firebase
firebase = firebase.FirebaseApplication("https://abhay-121-default-rtdb.firebaseio.com/", None)
import socket
import random
import sys
from kivy.core.video import Video
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import requests
import cv2
import numpy as np
import py2exe
from kivymd.uix.dialog import MDDialog

from PIL import Image
import time
from kivy.uix.image import Image, AsyncImage, CoreImage
from mutagen.id3 import ID3
from kivymd.toast import toast
import random

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatIconButton, MDIconButton, MDFlatButton, MDFloatingActionButton, MDTextButton
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager,FadeTransition
from kivy.clock import Clock
from kivy.uix.label import Label
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.taptargetview import MDTapTargetView
import cv2
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.video import Video
from kivy.uix.behaviors import ButtonBehavior
from kivy.factory import Factory
from kivy.uix.button import Button
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.behaviors import TouchBehavior
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.filemanager import MDFileManager
from kivy.core.text import LabelBase
from kivymd.uix.list import IRightBodyTouch,MDList, ThreeLineAvatarIconListItem,ThreeLineAvatarListItem,ImageLeftWidget,ThreeLineIconListItem,OneLineListItem,OneLineAvatarIconListItem,TwoLineAvatarIconListItem,IconLeftWidget, TwoLineAvatarListItem, OneLineAvatarListItem
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.spinner import MDSpinner
from kivy.network.urlrequest import UrlRequest
import os
from PIL import Image as PILimage
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
import time
from kivymd.uix.bottomsheet import MDListBottomSheet
#from kvdroid.tools.audio import Player
from kivymd.uix.pickers import MDTimePicker
from kivy.graphics.texture import Texture
from kivymd.uix.label import MDIcon
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
#from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
#from kivy.uix.screenmanager.WipeTransition import WipeTransition
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.fitimage import FitImage
import requests
from kivy.loader import Loader
import sys
import base64
import json
import os
import io
from kivymd.uix.tab import MDTabsBase
from kivy.utils import platform
from contextlib import closing
from threading import Thread

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import requests
import cv2
import numpy as np
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.properties import StringProperty
from kivymd.uix.navigationrail import MDNavigationRailItem



class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):
    '''
    Implements a button of type
    `Extended FAB <https://m3.material.io/components/extended-fab/overview>`_.

    .. rubric::
        Extended FABs help people take primary actions.
        They're wider than FABs to accommodate a text label and larger target
        area.

    This type of buttons is not yet implemented in the standard widget set
    of the KivyMD library, so we will implement it ourselves in this class.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)

    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            value = self.height / 4
            self.radius = [value, value, value, value]
            self._radius = value

class VideoStream(Image):
    def __init__(self, **kwargs):
        super(VideoStream, self).__init__(**kwargs)
        self.stream = None
        self.bytes_data = b""
        self.streaming = False  # Streaming flag

    def start_stream(self):
        self.stream = requests.get(self.url, stream=True)
        self.streaming = True
        Clock.schedule_interval(self.update, 1.0 / 90)

    def update(self, dt):
        response = requests.get(self.url, stream=True)
        bytes_data = bytes()
        for chunk in response.iter_content(chunk_size=8192):
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
        
   
class abhay(TwoLineAvatarIconListItem):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class HoverButton(Button, HoverBehavior):
    background = ListProperty((71/255, 104/255, 237/255, 1))
    def on_enter(self):
        self.background = (251/255, 104/255, 23/255, 1)
        Animation(size_hint= (.6, .1), d=.3).start(self)

    def on_leave(self):
        self.background = (71/255, 104/255, 237/255, 1)
        Animation(size_hint= (.3, .07), d=.3).start(self)

class HoverButton1(Button, HoverBehavior):
    background = ListProperty((71/255, 104/255, 237/255, 1))
    def on_enter(self):
        self.background = (251/255, 104/255, 23/255, 1)
        

    def on_leave(self):
        self.background = (71/255, 104/255, 237/255, 1)

class Videos(Video):
    pass

class MainApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    last_screen = []
    exit = "0"
    password = ""
    username = "abhay121"
    
    #win_size = min(Window.size)
    
    def build(self):
        screen = Builder.load_file("login.kv")
        self.theme_cls.accent_palette = self.theme_cls.primary_palette
        return screen
            
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard == 13:
            if self.root.ids.screen_manager.current == 'login_screen':
                self.login()
            else:
                pass
      
        if keyboard in (1001, 27):   
            if self.manager_open:
                self.file_manager.back()
            else:
                self.back_screen()
 
        return True
                
    def on_start(self, *args):
        
        DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
        LOCASE_CHARACTERS = ["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y",'z']
        SYMBOLS = ["@","#","$","%","&","/","?","="]

        COMBINED_List = random.choice(DIGITS) + random.choice(LOCASE_CHARACTERS) +random.choice(SYMBOLS)

        rand_digit = random.choice(DIGITS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        rand_list = random.choice(COMBINED_List)

        rand_digit1 = random.choice(DIGITS)
        rand_lower1 = random.choice(LOCASE_CHARACTERS)
        rand_symbol2 = random.choice(SYMBOLS)
        rand_list2 = random.choice(COMBINED_List)

        temp_pass = rand_digit + rand_lower + rand_symbol + rand_list + rand_digit1 + rand_lower1 + rand_symbol2 + rand_list2

        print(temp_pass)

        data = {
            "password":temp_pass
        }

        firebase.post("abhay-121-default-rtdb/Users/password", data)
        self.password = temp_pass
            
    def back_screen(self, *args):
        if self.root.ids.screen_manager.current != "homepage":
            self.change_screen(self.last_screen[-1], 'right')
            self.last_screen.pop(-1)
            
    def change_screen(self, screen, *args):
        if self.root.ids.screen_manager.current == 'homepage' or self.root.ids.screen_manager.current == "hl":
            try:
                pass
            except:
                pass
        if args:
            self.root.ids.screen_manager.transition.direction = args[0]
            if args[0] != 'right':
                self.last_screen.append(self.root.ids.screen_manager.current)
                
        else:
            self.root.ids.screen_manager.transition.direction = 'left'
            self.last_screen.append(self.root.ids.screen_manager.current)
        self.root.ids.screen_manager.current = screen

    def login(self):
        self.exit += "1"

        if self.exit == "0111":
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            data = {
                "ip_address":IPAddr
            }
            firebase.post("abhay-121-default-rtdb/Users/Threat", data)
            
            exit(0)
        else:
            pass

        
        username = self.root.ids.username.text

        if self.username == username:
            pass
        else:
            self.root.ids.username.text = ""
            self.root.ids.username.hint_text = "Enter Valid Username"
            toast("Wrong Username")

        password = self.root.ids.password.text
            
        if self.password == password:
            pass
        else:
            self.root.ids.password.text = ""
            self.root.ids.password.hint_text = "Enter Valid Password"
            toast("Wrong Password")

        if self.username == username and self.password == password:
            self.change_screen("homepage")
            toast("login successfully")
        else:
            pass

        self.root.ids.spinner.active = False
       
        

    def show_password(self, checkbox, value):
        if value:
            self.root.ids.password.password = False
            self.root.ids.password_text.text = "Hide Password"
        else:
            self.root.ids.password.password = True
            self.root.ids.password_text.text = "Show Password"


    def say1(self):
        toast("BSDK")
    def say2(self):
        toast("MKC")
    def say3(self):
        toast("MC")
    def say4(self):
        toast("F**K YOU")

        
MainApp().run()
