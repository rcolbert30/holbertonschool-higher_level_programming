#!/usr/bin/python3
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    aList = load_from_json_file('add_item.json')
except FileNotFoundError:
    aList = []
finally:
    for f in argv[1:]:
        aList.append(f)
    save_to_json_file(aList, 'add_item.json')
