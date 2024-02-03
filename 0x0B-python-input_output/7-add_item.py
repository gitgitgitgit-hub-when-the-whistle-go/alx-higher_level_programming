#!/usr/bin/python3
""" mixes the json from add_item.json with the argv form this module """

if __name__ == "__main__":
    import sys
    load_file = __import__('6-load_from_json_file').load_from_json_file
    save_file = __import__('5-save_to_json_file').save_to_json_file
    try:
        lis = load_file("add_item.json")
    except FileNotFoundError:
        lis = []
        print("not found")
    lis.extend(sys.argv[1:])
    save_file(lis, "add_item.json")
