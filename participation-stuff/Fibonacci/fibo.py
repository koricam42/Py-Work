"""
Author: Jordan Mensah


"""

def even_sum_fibonacci():
    """Finds the sum of even-valued terms in the fibonacci sequence lower than four million.
        returns:
            something: stuff to write here
    """

    uno, dos = 1, 2
    even_sum = 0
    while uno <= 4000000:
        if uno % 2 == 0:
            even_sum += uno
        return even_sum