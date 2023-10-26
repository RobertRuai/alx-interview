#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """
    determines if a given data set
    represents a valid UTF-8 encoding
    """
    bytes_to_process = 0
    
    for byte in data:
        if bytes_to_process > 0:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_process -= 1
        else:
            if (byte >> 7) == 0:
                bytes_to_process = 0
            elif (byte >> 5) == 0b110:
                bytes_to_process = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_process = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_process = 3
            else:
                return False
    
    return bytes_to_process == 0
