def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    n = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            n = n + 1
    if n != len(secretWord):
        return False
    else:
        return True  
