#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It handles both integers and floats, casting floats to integers.
If invalid input is given, it raises a TypeError.
"""

def add_integer(a, b=98):
    """Adds two integers or floats and returns the integer result."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
