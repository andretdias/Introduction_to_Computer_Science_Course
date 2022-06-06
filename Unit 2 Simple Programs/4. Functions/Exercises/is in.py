def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    elif aStr[round(len(aStr)/2)] == char:
        return True
    elif ord(char) < ord(aStr[round(len(aStr)/2)]):
        if len(aStr)%2 == 0:
            aStr = aStr[:int(round(len(aStr)/2))]
            return isIn(char, aStr)
        else:
            aStr = aStr[:int(round(len(aStr)/2))]
            return isIn(char, aStr)
    else:
        if len(aStr)%2 == 0:
            aStr = aStr[int(round(len(aStr)/2)):]
            return isIn(char, aStr)
        else:
            aStr = aStr[int(round(len(aStr)/2)):]
            return isIn(char, aStr)
