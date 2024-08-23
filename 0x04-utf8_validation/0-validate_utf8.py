#!/usr/bin/python3
"""
UTF-8 Validation Module
"""

def validUTF8(data):
    """
    Check if the data is a valid UTF-8 encoding.
    :param data: List of integers
    :return: True if data is valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check if the byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0

# Example usage
if __name__ == "__main__":
    data = [197, 130, 1]
    print(validUTF8(data))  # Output: True
