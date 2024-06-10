#!/usr/bin/python3
""""only if the obj is an instance of the class"""


def inherits_from(obj, a_class):
    """"return true if it is an instance of the class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
