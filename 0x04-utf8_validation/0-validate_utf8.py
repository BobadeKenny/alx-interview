#!/usr/bin/python3
"""UTF-8 validator"""


def validUTF8(data):
    """Checks if data is valid UTF-8 encoding"""
    n_bytes = 0
    for num in data:
        byte = format(num, '#010b')[-8:]
        if n_bytes == 0:
            if byte[0] == '1':
                n_bytes = len(byte.split('0')[0])
            if n_bytes > 4 or n_bytes == 1:
                return False
            if n_bytes == 0:
                continue
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False
        n_bytes -= 1
    return n_bytes == 0
