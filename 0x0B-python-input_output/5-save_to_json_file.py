#!/usr/bin/python3
""" a function that returns the JSON representation of an object (file) """


import json


def save_to_json_file(my_obj, filename):
    """ R T F moduledoc """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
