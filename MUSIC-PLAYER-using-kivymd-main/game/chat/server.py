# server.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

chat_history = []

@socketio.on('connect')
def handle_connect():
    # Send all stored messages to the newly connected client
    for msg in chat_history:
        emit('message', msg)

@socketio.on('message')
def handle_message(data):
    print(f"Message received: {data}")
    chat_history.append(data)
    emit('message', data, broadcast=True)  # Broadcast to all clients

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
