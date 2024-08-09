#!/usr/bin/python3
def minOperations(n):
    '''
    Calculate the minimum number of operations.int: The minimum number
    '''

    operations = 0  # Initialize the number of operations performed.
    factor = 2  # Start with the smallest prime factor.

    if n <= 1:
        return 0  # If n is 1 or less, no operations are needed.

    # Iterate until we reduce n to 1 by dividing it by its smallest factors.
    while n > 1:
        # If n is divisible by the current factor, divthe factor
        # and add the factor to the total operations count.
        if n % factor == 0:
            n = n / factor
            operations += factor
        else:
            factor += 1  # Increment the factor to check.
    return operations  # Return the total number of op.
