#!/usr/bin/pyhon3
""" a function that returns the JSON representation of an object (string) """


import json


def to_json_string(my_obj):
    """ R T F moduledoc """
    return json.dumps(my_obj)
