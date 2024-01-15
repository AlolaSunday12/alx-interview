#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to result in exactly n H characters in the file.

    Parameters:
    - n (int): Target number of H characters.

    Returns:
    - int: Fewest number of operations.
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2

    while i <= n:
        if n % i == 0:
            n //= i
            operations += i
        else:
            i += 1

    return operations
