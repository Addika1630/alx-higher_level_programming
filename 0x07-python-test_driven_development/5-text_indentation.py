#!/usr/bin/python3

"""
    Text Indentation
"""


def text_indentation(text):
    """print text 2 new lines after each of these characters: ., ? and :

    Args:
        text: text to be printed
    Raise
        TypeError: when text is not str
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    n = 0
    while n < len(text):
        if text[n] in [':', '.', '?']:
            print(text[n])
            print()
            n = n + 1
        else:
            print(text[n], end='')
        n += 1
