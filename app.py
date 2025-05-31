from flask import Flask
from flask_socketio import SocketIO
from auth.auth_routes import auth_blueprint
from terminal.shell_runner import terminal_blueprint
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key'
socketio = SocketIO(app)

# Register Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(terminal_blueprint)

if __name__ == "__main__":
    socketio.run(app, debug=True)
