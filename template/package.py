#!/usr/bin/env python3

class template():
    """docstring for template"""
    def __init__(self, x, y):
        super(template, self).__init__()
        self.__x = x
        self.__y = y

    def __str__(self):
        return str((self.__x, self.__y))

    def sum(self):
        return self.__x + self.__y

    def diff(self):
        return abs(self.__x - self.__y)

