#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        if n % factor == 0:
            n = n / factor
            operations += factor
        else:
            factor += 1
    
    return operations

