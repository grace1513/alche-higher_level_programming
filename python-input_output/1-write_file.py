#!/usr/bin/python3
"""Module that writes a string to a UTF-8 text file."""
def write_file(filename="", text=""):
    """Writes a string to a UTF-8 file and returns number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
