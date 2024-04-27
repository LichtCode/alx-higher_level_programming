#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    p_s1 = Square(5)
    print(p_s1)

    p_s1.update(10)
    print(p_s1)

    p_s1.update(1, 2)
    print(p_s1)

    p_s1.update(1, 2, 3)
    print(p_s1)

    p_s1.update(1, 2, 3, 4)
    print(p_s1)

    p_s1.update(x=12)
    print(p_s1)

    p_s1.update(size=7, y=1)
    print(p_s1)

    p_s1.update(size=7, id=89, y=1)
    print(p_s1)
