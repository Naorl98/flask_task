# Chat Room Application

## Overview
This project is a chat room application using Flask for the backend and a simple HTML/JavaScript frontend. It supports multiple chat rooms with message history saved in text files. The application ensures that chat history is preserved even after the server restarts. Users can interact with the chat room through a web interface that automatically updates every 1.5 seconds to display new messages.

## Features
- Multiple Chat Rooms: Users can participate in different chat rooms.
- Persistent Chat History: Chat history is saved in text files within the server.
- Automatic Chat Updates: The chat interface updates periodically to show new messages.

## Technologies
- Backend: Python, Flask
- Frontend: HTML, JavaScript (using jQuery for AJAX calls)
- Data Storage: Text files managed by the server

## Installation
To set up and run this application on your local machine, follow these steps:
1. Clone the repository.
2. Navigate to the project directory.
3. Install Flask.
4. Run the application.
This will start the Flask server on `http://127.0.0.1:5000/`.

## Usage
After starting the server, open your web browser and navigate to `http://127.0.0.1:5000/`. The application will redirect you to the default chat room (`/general`). You can access other chat rooms by modifying the URL (e.g., `http://127.0.0.1:5000/room-name`).

### Interacting with the Chat
- Sending Messages: Enter your username and message in the form provided and click 'send'. The message will appear in the chat window.
- Viewing Messages: Messages are displayed in real-time as they are received from other users.

## API Endpoints
- `GET /<room>`: Serves the chat room page.
- `POST /api/chat/<room>`: Receives new messages and saves them to the respective room's file.
- `GET /api/chat/<room>`: Retrieves all messages from the specified room.

## Future Improvements
- User Authentication: Implement user login functionality to manage access.
- Real-Time Communication: Upgrade to WebSocket for a real-time chat experience.
- UI Enhancements: Improve the user interface for a better user experience.

## Contributors
- Naor ladani

## License
This project is licensed under the MIT License - see the LICENSE file for details.
