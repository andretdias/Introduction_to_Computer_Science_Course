def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    b1 = b
    a1 = a
    if a > b:
        if a%b == 0:
            return b
        else:
            while a%b != 0 or b1%b != 0:
                b = b - 1
        return b
    elif a < b:
        if b%a == 0:
            return a
        else:
            while b%a != 0 or a1%a != 0:
                a = a - 1
        return a
