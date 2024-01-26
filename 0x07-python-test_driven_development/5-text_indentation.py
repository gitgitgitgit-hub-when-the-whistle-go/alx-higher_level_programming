#!/usr/bin/python3
""" module doc """


def text_indentation(text):
    """
    print in weird way lmao
    Args:
        text: the text
    Raises:
        TypeError: in case it's not a str
    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    # count the number of spaces encountered
    num_spaces = 0
    # if start of the line == 0 and 1 otherwise
    start = 0
    for i in range(len(text)):
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print(num_spaces * ' ', end='')
            num_spaces = 0
            start = 0
            print(text[i], end='')
            print('\n')
            continue
        if text[i] != ' ':
            print(start * num_spaces * ' ', end='')
            num_spaces = 0
            print(text[i], end='')
            start = 1
            continue
        else:
            num_spaces += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
