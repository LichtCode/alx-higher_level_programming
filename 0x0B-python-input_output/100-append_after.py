#!/usr/bin/python3

"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within each line of the file.
        new_string (str): The string to insert after each occurrence of the 
            search_string.
    """
    lines = []
    with open(filename) as r:
        for line in r:
            lines.append(line.rstrip())
            if search_string in line:
                lines.append(new_string)
    with open(filename, "w") as w:
        w.write("\n".join(lines))
