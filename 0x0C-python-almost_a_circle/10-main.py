#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    p_s1 = Square(5)
    print(p_s1)
    print(p_s1.size)
    p_s1.size = 10
    print(p_s1)

    try:
        p_s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
