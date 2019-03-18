def sum_array(array):
    '''
    Returns sum of all items in array

    Args:
        items (array): list or array-like object containing numerical values.

    Returns:
        int or float: returns the sum of all the elements in the array
    '''
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])
# end sum_array()


def fibonacci(n):
    '''
    Returns nth term in fibonacci sequence.
    Every number in the sequence is the sum of the preceding two numbers.

    Args:
        n int: positive integer for the term.

    Returns:
        int: returns nth term in fibonacci sequence.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
# end fibonacci


def factorial(n):
    '''
    Return n!

    Args:
        n int: positive integer for the nth factorial.

    Returns:
        int: returns n!
    '''
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
# end factorial


def reverse(word):
    ''''
    Return word in reverse.

    Args:
        word String: string to be reversed.

    Returns:
        string: reversed string from word
    '''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
# end reverse
