#!/usr/bin/python3
"""Checks whether object is an instance"""


def inherits_from(obj, a_class):
    """Is obj a subclass of a_class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
