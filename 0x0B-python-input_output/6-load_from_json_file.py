#!/usr/bin/python3
""" returns an object (Python data structure) represented by a JSON string """


import json


def load_from_json_file(filename):
    """ as mod doc says xD """
    return json.load(filename)
