"""
Author: Jordan Mensah
Date: 10/2/26
Source Code (References):
    - Fibonacci Sequence Help: https://pythonguides.com/python-fibonacci-series/
    - More Fibonacci Stuff: https://www.geeksforgeeks.org/python/python-program-for-n-th-fibonacci-number/
    - Modulo Operator Help: https://www.geeksforgeeks.org/python/what-is-a-modulo-operator-in-python/
"""

def even_sum_fibonacci():
    """Finds the sum of even-valued terms in the fibonacci sequence lower than four million.
        returns:
            int: Total sum of even valued terms in the fibonacci sequence < 4,000,000
    """

    current1, next1 = 1, 2
    even_sum = 0

    while current1 <= 4000000:
        if current1 % 2 == 0:
            even_sum += current1


        temp1 = current1
        current1 = next1
        next1 = temp1 + next1

    return even_sum

print(even_sum_fibonacci())