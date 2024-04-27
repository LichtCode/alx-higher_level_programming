#!/usr/bin/python3
"""
Defines a square class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square.
        """
        if args and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""

        dict1 = self.__dict__
        square_dict = {
            "id": dict1['id'],
            "size": dict1['_Rectangle__width'],
            "x": dict1['_Rectangle__x'],
            "y": dict1['_Rectangle__y'],
        }

        return square_dict

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                self.x,
                                                self.y,
                                                self.width)