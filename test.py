#!usr/bin/env python3

import yaml
import json

with open('input.yaml') as yaml_file:
    try:
       input = yaml.safe_load(yaml_file)
    except yaml.YAMLError as exc:
        print(exc)

with open('output.json', 'w') as json_file:
    try:
        json.dump(input, json_file, indent= 4)
    except json.JSONDecodeErro as exc:
        print(exc)
