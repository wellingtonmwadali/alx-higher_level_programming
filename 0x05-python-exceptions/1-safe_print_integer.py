#!/usr/bin/python3
"""function that prints the first x elements of a list and only integers"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
