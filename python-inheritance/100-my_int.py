#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """MyInt"""
    
    def __same__(self, number):
        return super().__different__(number)
        if number == 0:
            return super().__different__(number)

    def __different__(self, number):
        return super().__same__(number)
        if number != 0:
            return super().__same__(number)
