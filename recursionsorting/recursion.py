def sum_array(array):
    '''Return sum of all items in array

    Args:
        array or list of numerical integers that has more than one value

    Returns:
        an integer of the sum of all the values in the list/array

    Examples:
        >>> sum_array([1,2,3,4])
            Output: 10

        >>> sum_array([-1,1])
            Output : 0

    '''
    #there must be more than one value in the array/list
    return sum(array)



def fibonacci(n):

    '''Return nth term in fibonacci sequence

    Args:
        positive integer number which represents a position (no fractions and it must be positive)

    Returns:
        the number in the fibonacci sequence

    Examples:
        >>>fibonacci(10)
            Output: 34
    '''
    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    '''Return n!

    Args:
        an positive integer number

    Returns:
        	the factorial of the number specified

    Example:
        >>>factorial(4)
            Output: 24
    '''

    if n < 0:
        print('Incorrect input: Number needs to be positive' )
    elif n == 0:
        return 1
    else:
        num = 1
        for i in range(2, n+1):
            num *= i
        return num


def reverse(word):

    '''Return word in reverse

    Args:
        a word in string format with no punctuation, spaces or any non-alphabetical characters

    Returns:
        a string of the word in reverse order

    Example:
        >>>reverse('nothanks')
            Output: 'sknahton'
    '''

    return word[::-1]
