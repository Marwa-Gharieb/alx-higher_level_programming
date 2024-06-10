#!/usr/bin/python3
""""Mylist inherts from list"""


class MyList(list):
    def print_sorted(self):
        list = self.sort()
        return list
