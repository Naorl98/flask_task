from flask import Flask, request, jsonify, send_from_directory, Response, redirect
import os
import datetime

app = Flask(__name__)

# Dictionary to store chat messages
chat_rooms = {}


@app.route('/', methods=['GET'])
def redirect_to_default_room():
    """Redirect to the default chat room."""
    print("Redirecting to the default chat room: general")
    return redirect('/general')


@app.route('/<room>', methods=['GET'])
def home(room):
    """Serve the static HTML file."""
    return send_from_directory(os.path.join(app.root_path), 'index.html')


@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    """Return all chat messages in a room."""
    room_messages = chat_rooms.get(room, [])
    print(f"Retrieving messages for room: {room}. Messages count: {len(room_messages)}")
    return Response(''.join(room_messages), mimetype='text/plain')


@app.route('/api/chat/<room>', methods=['POST'])
def post_chat(room):
    """Receive a chat message and store it in the room."""
    username = request.form.get('username')
    message = request.form.get('msg')
    if not username or not message:
        print("Error: Missing username or message")
        return jsonify({"error": "Missing data"}), 400

    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_message = f"{timestamp} {username}: {message}\n"

    if room not in chat_rooms:
        chat_rooms[room] = []
    chat_rooms[room].append(full_message)

    print(f"Message added to room {room}: {full_message.strip()}")
    return jsonify({"success": True, "message": "Message added"})


if __name__ == '__main__':
    app.run(debug=True)
