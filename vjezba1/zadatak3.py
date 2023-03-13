BINGO = 0
LOWER = -1
HIGHER = 1

import random

def generateTarget(rangeDown, rangeUp):
    return random.randint(rangeDown, rangeUp)

def checkGuess(guess, target):
    if guess == target:
        return BINGO
    elif guess < target:
        return HIGHER
    else:
        return LOWER
    
def validNumber(rangeDown, rangeUp, guess):
    if guess >= rangeDown and guess < rangeUp:
        return True
    else:
        return False

def main():
    rangeDown = 0
    rangeUp = 1001
    guess = -1
    endGame = False
    target = generateTarget(rangeDown, rangeUp)
    while not endGame:
        print("< ", rangeDown, ", ", rangeUp - 1, ">")
        guess = int(input("Your guess: "))

        if validNumber(rangeDown, rangeUp, guess):
            resolve = checkGuess(guess, target)
            if resolve == HIGHER:
                rangeDown = guess
                print("HIGHER")
            elif resolve == LOWER:
                rangeUp = guess
                print("LOWER")
            else:
                print("BINGO")
                endGame = True
        else:
            print("Your Guess is out of range")

main()