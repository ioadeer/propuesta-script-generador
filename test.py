#!usr/bin/env python3

#import yaml
import json
from models.Room import Room

with open('input.json') as json_file:
    try:
        input = json.load(json_file)
    except json.JSONDecodeError as exc:
        print(exc)


room = Room(input['room'])

room.dump_room_info()

with open('output.json', 'w') as json_file:
    try:
        json.dump(input, json_file, indent= 4)
    except json.JSONDecodeError as exc:
        print(exc)
