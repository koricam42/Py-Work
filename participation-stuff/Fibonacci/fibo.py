"""
Author: Jordan Mensah


"""

def even_sum_fibonacci():
    """Finds the sum of even-valued terms in the fibonacci sequence lower than four million.
        returns:
            something: stuff to write here
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