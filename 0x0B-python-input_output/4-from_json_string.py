#!/usr/bin/python3
""" returns an object (Python data structure) represented by a JSON string """


import json


def from_json_string(jsonObj):
    """ as mod doc says xD """
    return json.loads(jsonObj)
