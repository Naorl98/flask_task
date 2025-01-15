from flask import Flask, request, jsonify, send_from_directory, Response, redirect
import os
import datetime

app = Flask(__name__)
chat_directory = "chat_files"

if not os.path.exists(chat_directory):
    os.makedirs(chat_directory)


def get_file_path(room):
    return os.path.join(chat_directory, f"{room}.txt")

def read_chat(room):
    file_path = get_file_path(room)
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return file.readlines()

def write_chat(room, message):
    file_path = get_file_path(room)
    with open(file_path, "a") as file:
        file.write(message)

@app.route('/', methods=['GET'])
def redirect_to_default_room():
    """Redirect to the default chat room."""
    return redirect('/general')

@app.route('/<room>', methods=['GET'])
def home(room):
    """Serve the static HTML file."""
    return send_from_directory(app.root_path, 'index.html')

@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    """Return all chat messages in a room."""
    room_messages = read_chat(room)
    return Response(''.join(room_messages), mimetype='text/plain')

@app.route('/api/chat/<room>', methods=['POST'])
def post_chat(room):
    """Receive a chat message and store it in the room."""
    username = request.form.get('username')
    message = request.form.get('msg')
    if not username or not message:
        return jsonify({"error": "Missing data"}), 400

    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_message = f"{timestamp} {username}: {message}\n"
    write_chat(room, full_message)
    return jsonify({"success": True, "message": "Message added"})

if __name__ == '__main__':
    app.run(debug=True)
