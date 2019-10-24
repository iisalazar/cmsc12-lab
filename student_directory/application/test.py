#!/usr/bin/python3
import json

with open('users.json') as f:
    data = json.loads(f.read())

from pprint import pprint
pprint(data)