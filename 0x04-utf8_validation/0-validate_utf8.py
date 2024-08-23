#!/usr/bin/python3
"""
Module for UTF-8 validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers where each integer represents 1 byte of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    for num in data:
        # Get the 8 least significant bits of the number
        byte = num & 255

        if n_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            if byte >> 5 == 0b110:
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                n_bytes = 3
            elif byte >> 7:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1

    # All characters should be complete
    return n_bytes == 0
