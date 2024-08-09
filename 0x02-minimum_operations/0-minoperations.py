#!/usr/bin/python3
def minOperations(n):
    '''
    Calculate the minimum number of operations.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required, or 0 if `n` is to 1.
    '''

    operations = 0
    factor = 2

    if n <= 1:
        return 0

    while n > 1:
        if n % factor == 0:
            n = n / factor
            operations += factor
        else:
            factor += 1
    return operations
