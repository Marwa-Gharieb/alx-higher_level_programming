#!/usr/bin/python3
"""adds two integers or floats.
      Args:
        a (int): The first integer.
        b (int): The second integer.
    Returns: int: The sum of a and b."""


def add_integer(a, b=98):

    """ Returns: int: The sum of a and b.
     Raises:
         TypeError: If either of a or b is not an integer or float."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
