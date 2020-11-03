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

room.door.frame.x
room.camera.posX

print(f'{room.door.halfDepth}')
room_surface = room.depth * room.width

print(f'{room_surface}')


roomString = room.dump_room_info()

print(f'{roomString}')

print(room.spot.posX)

with open('output.json', 'w') as json_file:
    try:
        json.dump(input, json_file, indent= 4)
    except json.JSONDecodeError as exc:
        print(exc)
