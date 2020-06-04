#!/usr/bin/python3
"""This module save arguments into a JSON file
"""
from sys import argv
save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file
try:
    data = load("add_item.json")
except:
    data = []
data.extend(argv[1:])
save(data, "add_item.json")
