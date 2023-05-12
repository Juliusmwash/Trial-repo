#!/usr/bin/python3
import json

s = '1123456, {"juli": "my_name", "age": 78}'
d = s.split(', ', maxsplit=1)[1]
print(d)
print(type(d))
e = json.loads(d)
print(e)
print(type(e))
