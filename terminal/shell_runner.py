from flask import Blueprint, render_template
from flask_socketio import emit
import pexpect
from explain.explain import explain_command

terminal_blueprint = Blueprint('terminal', __name__)

@terminal_blueprint.route('/terminal')
def terminal_view():
    return render_template('terminal.html')

# Reference socketio instance from app
from app import socketio

@socketio.on('command')
def handle_command(data):
    command = data['command']
    try:
        shell = pexpect.spawn('/bin/bash', ['-c', command], encoding='utf-8')
        shell.expect(pexpect.EOF)
        output = shell.before
    except Exception as e:
        output = f"Error executing command: {str(e)}"

    explanation = explain_command(command)
    emit('response', {
        'output': output,
        'description': explanation['description'],
        'example': explanation['example'],
        'risk': explanation['risk']
    })
