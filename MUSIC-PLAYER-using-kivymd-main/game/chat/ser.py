from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Store chat history in memory (for demonstration purposes)
chat_history = []


@socketio.on('send_message')
def handle_send_message(message):
    # Append message to chat history
    chat_history.append(message)
    # Broadcast message to all connected clients
    emit('receive_message', message, broadcast=True)

@socketio.on('get_chat_history')
def handle_get_chat_history():
    # Send the chat history to the user
    emit('receive_chat_history', chat_history)

if __name__ == '__main__':
    socketio.run(app, debug=True)