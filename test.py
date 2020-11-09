#!usr/bin/env python3

#import yaml
import json
import os
from pathlib import Path
from models.Room import Room

with open('input.json') as json_file:
    try:
        input = json.load(json_file)
    except json.JSONDecodeError as exc:
        print(exc)


room = Room(input['room'])

room.door.frame.width
print(f'Camera x position value {room.camera.x}')

print(f'{room.door.position}')
room_surface = room.depth * room.width

#print(f'{room_surface}')
print('Room docstring help \n')

help(room)
#print(f'Room init method help string: {}')
roomString = room.dump_room_info()

print(f'{roomString}')

print(room.spot.x)
aPath = Path(os.path.realpath(__file__)).parents[0]
print(aPath)
print(os.path.realpath(__file__))

with open('output.json', 'w') as json_file:
    try:
        json.dump(input, json_file, indent= 4)
    except json.JSONDecodeError as exc:
        print(exc)
