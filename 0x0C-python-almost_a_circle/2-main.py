#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))

    try:
        p_r = Rectangle(10, 2)
        p_r.width = -10
    except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))

    try:
        p_r = Rectangle(10, 2)
        p_r.x = {}
    except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))
