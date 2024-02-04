#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    """ class to json """
    import json
    return json.dumps(dir(obj))
