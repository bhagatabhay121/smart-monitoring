# chat_app.py
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
import socketio

KV = '''
ScreenManager:
    ChatScreen:

<ChatScreen>:
    name: 'chat'

    MDBoxLayout:
        orientation: 'vertical'

        ScrollView:
            MDList:
                id: message_list

        MDBoxLayout:
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)

            MDTextField:
                id: message_input
                hint_text: "Type a message..."
                multiline: False
                size_hint_x: 0.8

            MDRaisedButton:
                text: "Send"
                on_release: app.send_message()
'''

class ChatScreen(Screen):
    pass

class ChatApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sio = socketio.Client()
        self.sio.on('message', self.receive_message)

    def build(self):
        self.connect_to_server()
        return Builder.load_string(KV)

    def connect_to_server(self):
        try:
            self.sio.connect('http://localhost:5000')  # Backend server URL
        except Exception as e:
            print(f"Failed to connect to server: {e}")

    def send_message(self):
        # Get the user's message
        message = self.root.get_screen('chat').ids.message_input.text
        if message.strip():
            # Send the message to the server
            self.sio.emit('message', {"message": message, "sender": "abhay"})
            # Add the message to the UI locally without waiting for the broadcast
            self.add_message_to_ui(f"You: {message}")
            self.root.get_screen('chat').ids.message_input.text = ""

    def receive_message(self, data):
        # Avoid re-adding messages sent by "You"
        if data.get("sender") != "abhay":
            sender = data.get("sender", "Other")
            message = data.get("message", "")
            # Update the UI safely on the main thread
            Clock.schedule_once(lambda dt: self.add_message_to_ui(f"{sender}: {message}"))

    def add_message_to_ui(self, message):
        # Add the message to the chat message list
        message_list = self.root.get_screen('chat').ids.message_list
        message_list.add_widget(OneLineListItem(text=message))

    def on_stop(self):
        # Disconnect the socket on app exit
        self.sio.disconnect()

if __name__ == '__main__':
    ChatApp().run()
