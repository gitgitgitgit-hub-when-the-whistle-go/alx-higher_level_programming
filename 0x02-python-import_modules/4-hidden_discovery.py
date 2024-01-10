#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    listf = dir(hidden_4)
    for e in listf:
        if e[0] != '_' and e[1] != '_':
            print(e)
