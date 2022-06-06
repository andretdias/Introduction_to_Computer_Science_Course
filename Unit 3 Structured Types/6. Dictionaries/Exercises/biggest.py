animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    length = []
    for element in aDict.values():
        length.append(len(element))
    maxlength = max(length)
    for element in aDict.keys():
        if len(aDict[element]) == maxlength:
            biggest = element
    return biggest

print(biggest(animals))
