#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ UTF-8 Validation """
    remaining = 0
    for num in data:
        if remaining == 0:
            if num >> 7 == 0b0:
                remaining = 0
            elif num >> 5 == 0b110:
                remaining = 1
            elif num >> 4 == 0b1110:
                remaining = 2
            elif num >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if num >> 6 == 0b10:
                remaining -= 1
            else:
                return False

    if remaining == 0:
        return True
    else:
        return False
