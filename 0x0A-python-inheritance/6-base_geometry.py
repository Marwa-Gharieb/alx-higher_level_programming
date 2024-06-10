#!/usr/bin/python3
""""module to create a class"""


BaseGeometry = __import__('5-base_geometry').BaseGeometry


class BaseGeometry:
    """"raise Exception"""
    def area(self):
        raise Exception("area() is not implemented")
