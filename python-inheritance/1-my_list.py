#!/usr/bin/python3
"""Inheritance List in Class MyList"""


class MyList(list):
    """MyList"""

    def print_sorted(self):
        """prints sorted list"""
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
