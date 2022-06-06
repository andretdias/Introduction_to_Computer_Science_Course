def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    availableletters = alphabet
    for letter in lettersGuessed:
        if letter in alphabet:
            availableletters = availableletters.replace(letter,'')
    return availableletters
