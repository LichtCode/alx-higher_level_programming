#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    p_r1 = Rectangle(3, 2)
    print(p_r1.area())

    p_r2 = Rectangle(2, 10)
    print(p_r2.area())

    p_r3 = Rectangle(8, 7, 0, 0, 12)
    print(p_r3.area())
