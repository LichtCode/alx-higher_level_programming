#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Converts float arguments to integers before addition.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
