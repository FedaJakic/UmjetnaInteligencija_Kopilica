BINGO = 0
LOWER = -1
HIGHER = 1

import random

def generateGuess(rangeDown, rangeUp):
    return random.randint(rangeDown, rangeUp)

def checkGuess():
    while True:
        resolve = input("Is my Guess correct.... (y/n)")
        if resolve.lower() == "y":
            return BINGO
        elif resolve.lower() == "n":
            resolve = input("Is my Guess lower or higher.... (l/h)")
            if resolve.lower() == "l":
                return LOWER
            elif resolve.lower() == "h":
                return HIGHER
            else:
               print("Incorect answer!") 
        else:
            print("Incorect answer!")
    
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
    print("Imagine number beetwem <", rangeDown, ",", rangeUp, ">")
    while not endGame:
        guess = generateGuess(rangeDown, rangeUp)
        print("My Guess is [", guess, "]")

        if validNumber(rangeDown, rangeUp, guess):
            resolve = checkGuess()
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
            print("Invalid guess")

main()