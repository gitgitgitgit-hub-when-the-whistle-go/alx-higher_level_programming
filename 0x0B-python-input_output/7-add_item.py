#!/usr/bin/python3
""" mixes the json from add_item.json with the argv form this module """


import sys


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

lis = sys.argv[1:]
lis.extend(load_file("add_item.json"))
save_file(lis, "add_item.json")
