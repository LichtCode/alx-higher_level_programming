#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    p_r1 = Rectangle(10, 2)
    print(p_r1.id)

    p_r2 = Rectangle(2, 10)
    print(p_r2.id)

    p_r3 = Rectangle(10, 2, 0, 0, 12)
    print(p_r3.id)
