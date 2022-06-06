def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    newTup = []
    n = -1
    for element in aTup:
        n = n + 1
        if n%2 == 0:
            newTup.append(element)
    return tuple(newTup)
