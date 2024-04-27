#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    p_r1 = Rectangle(10, 7, 2, 8)
    p_r2 = Rectangle(2, 4)
    Rectangle.save_to_file([p_r1, p_r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
