from flask import Flask, request, jsonify, send_from_directory, Response, redirect
import os
import datetime

app = Flask(__name__)
chat_directory = "chat_files"

# Create a directory to store chat messages if it does not exist
if not os.path.exists(chat_directory):
    os.makedirs(chat_directory)
# Implemented by ilia
def get_file_path(room):
    """Return the file path for a specific chat room."""
    return os.path.join(chat_directory, f"{room}.txt")
# Implemented by ilia
def read_chat(room):
    """Read messages from the chat file for a specific room."""
    file_path = get_file_path(room)
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return file.readlines()
# Implemented by naor
def write_chat(room, message):
    """Write a message to the chat file of a specific room."""
    file_path = get_file_path(room)
    with open(file_path, "a") as file:
        file.write(message)
# Implemented by naor
@app.route('/', methods=['GET'])
def redirect_to_default_room():
    """Automatically redirect to the default chat room."""
    return redirect('/general')

@app.route('/<room>', methods=['GET'])
def home(room):
    """Serve the static HTML file for the user interface."""
    return send_from_directory(app.root_path, 'index.html')
# Implemented by ilia
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    """Return all messages in a specific chat room as a text response."""
    room_messages = read_chat(room)
    return Response(''.join(room_messages), mimetype='text/plain')
# Implemented by naor
@app.route('/api/chat/<room>', methods=['POST'])
def post_chat(room):
    """Receive a new message from the user and store it in the appropriate chat room."""
    username = request.form.get('username')
    message = request.form.get('msg')
    if not username or not message:
        return jsonify({"error": "Missing data"}), 400

    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_message = f"{timestamp} {username}: {message}\n"
    write_chat(room, full_message)
    return jsonify({"success": True, "message": "Message added"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
