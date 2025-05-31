import json
import os

data_file = os.path.join(os.path.dirname(__file__), 'command_explanations.json')

with open(data_file, 'r') as f:
    EXPLAIN_DATA = json.load(f)

def explain_command(command):
    cmd = command.strip().split()[0]
    return EXPLAIN_DATA.get(cmd, {
        "description": "No explanation available.",
        "example": "N/A",
        "risk": "Unknown"
    })
