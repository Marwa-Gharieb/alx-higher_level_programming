#!/usr/bin/python3
""""test if it is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """"returns True if the object is exactly an instance of the class"""
    if obj.__class__ == a_class or isinstance(obj, a_class):
        return True
    else:
        return False
