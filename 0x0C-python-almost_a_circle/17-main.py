#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    p_r1 = Rectangle(3, 5, 1)
    p_r1_dictionary = p_r1.to_dictionary()
    p_r2 = Rectangle.create(**p_r1_dictionary)
    print(p_r1)
    print(p_r2)
    print(p_r1 is p_r2)
    print(p_r1 == p_r2)
