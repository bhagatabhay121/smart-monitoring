# Real-time Chat Application using KivyMD

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import socket
import threading

KV = '''
ScreenManager:
    ChatScreen:

<ChatScreen>:
    name: 'chat'
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'horizontal'
            MDTextField:
                id: message_input
                hint_text: "Type your message"
                multiline: False
            MDRaisedButton:
                text: "Send"
                on_release: app.send_message()
        MDBoxLayout:
            id: chat_box
            orientation: 'vertical'
'''

class ChatScreen(Screen):
    pass

class ChatApp(MDApp):
    def build(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 12345))
        self.server_socket.listen(5)
        threading.Thread(target=self.accept_connections, daemon=True).start()
        return Builder.load_string(KV)

    def accept_connections(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()

    def handle_client(self, client_socket):
        while True:
            message = client_socket.recv(1024).decode()
            if message:
                self.update_chat_box(message)

    def update_chat_box(self, message):
        self.root.ids.chat_box.add_widget(MDLabel(text=message, halign='left'))

    def send_message(self):
        message = self.root.ids.message_input.text
        if message:
            self.update_chat_box(f"You: {message}")
            self.root.ids.message_input.text = ''
            # Here you would send the message to the server
            # client_socket.send(message.encode())

if __name__ == '__main__':
    ChatApp().run()
