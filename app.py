from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = 'super_secret_key'
socketio = SocketIO(app)

# Import routes AFTER app is defined
from auth.auth_routes import auth_blueprint
from terminal.shell_runner import terminal_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(terminal_blueprint)
