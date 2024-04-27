#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    p_s1 = Square(10, 2, 1)
    print(p_s1)
    s1_dictionary = p_s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(p_s1 == s2)
