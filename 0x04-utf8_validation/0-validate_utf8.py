#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes to process
    number_of_bytes = 0

    # Masks to identify the type of byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            # Count how many leading 1s
            while mask & byte:
                number_of_bytes += 1
                mask = mask >> 1
            
            # 1-byte character or invalid UTF-8
            if number_of_bytes == 0:
                continue
            
            # UTF-8 can only be 1 to 4 bytes long
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the count of bytes left to check
        number_of_bytes -= 1

    # If there are no leftover bytes to check, it's valid
    return number_of_bytes == 0

