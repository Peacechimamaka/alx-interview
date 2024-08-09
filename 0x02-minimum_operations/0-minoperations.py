#!/usr/bin/python3
def minOperations(n):
    ''' 
    Calculate the minimum number of operations required to achieve exactly `n` characters in a text file,
    starting with one character and using only copy-all and paste operations.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations required, or 0 if `n` is less than or equal to 1.
    '''
    
    operations = 0  # Initialize the number of operations performed.
    factor = 2  # Start with the smallest prime factor.

    if n <= 1:
        return 0  # If n is 1 or less, no operations are needed.

    # Iterate until we reduce n to 1 by dividing it by its smallest factors.
    while n > 1:
        # If n is divisible by the current factor, divide n by the factor
        # and add the factor to the total operations count.
        if n % factor == 0:
            n = n / factor
            operations += factor
        else:
            factor += 1  # Increment the factor to check the next possible divisor.

    return operations  # Return the total number of operations required.

