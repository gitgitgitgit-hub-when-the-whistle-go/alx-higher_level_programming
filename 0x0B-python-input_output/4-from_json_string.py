#!/usr/bin/python3
""" returns an object (Python data structure) represented by a JSON string """


from json import load


def from_json_string(jsonObj):
    """ as mod doc says xD """
    return load(jsonObj)
