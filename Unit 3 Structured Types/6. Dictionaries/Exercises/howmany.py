animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    n = 0
    for element in aDict.values():
        if len(element) == 1:
            n = n + 1
        else:
            for ele in element:
                n = n + 1
    return n

print(how_many(animals))
