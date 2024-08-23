#!/usr/bin/python3

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list): A list of integers, each representing 1 byte of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    # Initialize a counter to track the number of bytes in a multi-byte character
    byte_count = 0

    for num in data:
        # Convert the integer to binary and remove the '0b' prefix
        binary = bin(num)[2:].zfill(8)

        # If we're not in the middle of a multi-byte character
        if byte_count == 0:
            # Check for 1-byte character
            if binary[0] == '0':
                continue
            # Check for 2-byte character
            elif binary[:3] == '110':
                byte_count = 1
            # Check for 3-byte character
            elif binary[:4] == '1110':
                byte_count = 2
            # Check for 4-byte character
            elif binary[:5] == '11110':
                byte_count = 3
            else:
                return False
        else:
            # Check for continuation byte
            if binary[:2] != '10':
                return False
            # Decrement the byte count
            byte_count -= 1

    # If we've finished processing all bytes and we're not in the middle of a character
    return byte_count == 0
