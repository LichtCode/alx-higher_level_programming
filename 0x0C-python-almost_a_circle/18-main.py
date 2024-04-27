#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    p_r1 = Rectangle(10, 7, 2, 8)
    p_r2 = Rectangle(2, 4)
    p_list_rectangles_input = [p_r1, p_r2]

    Rectangle.save_to_file(p_list_rectangles_input)

    list_r_output = Rectangle.load_from_file()

    for rect in p_list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_r_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    p_s1 = Square(5)
    p_s2 = Square(7, 9, 1)
    list_s_input = [p_s1, p_s2]

    Square.save_to_file(list_s_input)

    list_s_output = Square.load_from_file()

    for square in list_s_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_s_output:
        print("[{}] {}".format(id(square), square))
