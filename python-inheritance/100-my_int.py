#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """MyInt"""

    def __eq__(self, number):
        return super().__ne__(number)

    def __ne__(self, number):
        return super().__eq__(number)
