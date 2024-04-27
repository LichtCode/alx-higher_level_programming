#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    p_r1 = Rectangle(10, 10, 10, 10)
    print(p_r1)

    p_r1.update(89)
    print(p_r1)

    p_r1.update(89, 2)
    print(p_r1)

    p_r1.update(89, 2, 3)
    print(p_r1)

    p_r1.update(89, 2, 3, 4)
    print(p_r1)

    p_r1.update(89, 2, 3, 4, 5)
    print(p_r1)
