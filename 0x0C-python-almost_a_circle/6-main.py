#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    p_r1 = Rectangle(2, 3, 2, 2)
    p_r1.display()

    print("---")

    p_r2 = Rectangle(3, 2, 1, 0)
    p_r2.display()
