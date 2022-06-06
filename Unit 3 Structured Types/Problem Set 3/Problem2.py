def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = secretWord
    for letter in secretWord:
        if letter not in lettersGuessed:
            guess = guess.replace(letter, ' _ ')
    return guess
