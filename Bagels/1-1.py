import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number')
        print('I have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guesse {}'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break

            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}'.format(secretNum))
        print('Do you waant to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing')



def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''.join(numbers[0:NUM_DIGITS])
    return secretNum

def getClues(guess, secretNum):

    clues = list()

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')


    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()