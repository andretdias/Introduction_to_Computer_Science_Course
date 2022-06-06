highcap = 100
lowcap = 0
guess = ''
print('Please think of a number between 0 and 100!')
while guess != 'c':
    midcap = (highcap + lowcap)/2
    print('Is your secret number ' + str(int(midcap)) + '?')
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess == 'h':
        highcap = int(midcap)
    elif guess == 'l':
        lowcap = int(midcap)
    elif guess == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
        continue
print('Game over. Your secret number was:', int(midcap))
