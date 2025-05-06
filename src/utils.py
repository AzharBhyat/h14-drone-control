from math import floor
import json

def seconds_to_reps(time: float):
    return floor(time/0.04)

def load_commands_dict(json_path="commands.json"):
    with open(json_path, "r") as file:
        raw_data = json.load(file)
    # Convert hex strings to bytes
    command_dict = {
        name: bytes.fromhex(value)
        for name, value in raw_data.items()
    }
    return command_dict