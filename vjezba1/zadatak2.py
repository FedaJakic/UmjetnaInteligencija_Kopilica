
def checkForSize(firstNumber, secondNumber):
    if(len(firstNumber) != len(secondNumber)):
        return False
    return True

def isContainingSameNumbers(firstNumber, secondNumber):
    checkedNumbers = []
    for i in range(len(firstNumber)):
        if isAlreadyChecked(checkedNumbers, firstNumber[i]):
            continue
        else:
            if(firstNumber[i] != secondNumber[i]):
                return "Brojevi nisu isti"

            checkedNumbers.append(firstNumber[i])

    return "Brojevi su isti"

def isAlreadyChecked(checkedNumbers, target):
    for number in checkedNumbers:
        if number == target:
            return True
    
    else:
        return False

def checkNumbers(firstNumber, secondNumber):
    strSortedFirst = sorted(str(firstNumber))
    strSortedSecond = sorted(str(secondNumber))

    if not checkForSize(strSortedFirst, strSortedSecond):
        return "Not same length"

    return isContainingSameNumbers(strSortedFirst, strSortedSecond)

def main():
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))

    print(checkNumbers(firstNumber, secondNumber))

main()