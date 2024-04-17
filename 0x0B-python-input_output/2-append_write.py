#!/usr/bin/python3

"""a file-appending function."""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a 
        text file (UTF8), Returns the number of characters.
    Args:
        filename (str): name of the file to append to.
        text (str): string to append to the file.
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
