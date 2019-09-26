# ----------------------------------------------------------------------
# Name:     generators
# Purpose:  Practice with Python generators
#
# Author:   Rula Khayrallah
# ----------------------------------------------------------------------
"""
Practice writing and using generator functions

A doubling sequence generator.
An infinite doubling sequence generator.
A hailstone sequence generator.
"""

def double_generator(limit):
    """
    Generate a sequence of powers of 2 starting at 1 and up to and
    including the limit specified.
    :param limit: (integer) upper limit of the sequence generated
    :yield: (integer) a power of two
    """
    current = 1
    while current <= limit:
        yield current
        current = current * 2

def infinite_double_generator():
    """
    Generate an infinite sequence of of powers of 2
    :yield:  (integer) a power of two
    """
    current = 1
    while True:
        yield current
        current = current * 2

def hailstone(number):
    while(number >1):
        yield number
        if(number%2 == 0): #even
            number = number / 2
        else: #odd
            number = number * 3 + 1
    yield number