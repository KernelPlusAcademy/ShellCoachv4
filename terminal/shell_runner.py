from flask import Blueprint, render_template
from flask_socketio import emit, join_room
import pexpect

terminal_blueprint = Blueprint('terminal', __name__)

@terminal_blueprint.route('/terminal')
def terminal_view():
    return render_template('terminal.html')

def spawn_shell():
    shell = pexpect.spawn('/bin/bash', encoding='utf-8')
    return shell

from app import socketio

@s...
