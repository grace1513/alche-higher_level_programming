#!/usr/bin/python3
"""Module that appends a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 file, return number of chars added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
