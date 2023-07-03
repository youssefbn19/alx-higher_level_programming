#!/usr/bin/python3
"""
Module contains print_square function that
prints a given text with new lines in specific characters
"""


def text_indentation(text):
    """
    The function that prints a text with 2 new lines
    after each pf these characters: . ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for pos in range(len(text)):
        if text[pos] == " " and text[pos - 1] in [".", "?", ":"]:
            continue
        print("{}".format(text[pos]), end="")
        if text[pos] in [".", "?", ":"]:
            print("\n")
