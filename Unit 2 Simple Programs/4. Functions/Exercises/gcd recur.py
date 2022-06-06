def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a%b == 0:
        return b
    elif b%a == 0:
        return a
    else:
        return gcdRecur(b, a%b)
