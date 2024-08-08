#!/usr/bin/python3
def minOperations(n):
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

