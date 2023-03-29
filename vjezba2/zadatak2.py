def dataSearch(target, testList):
    if(len(testList) == 0):
        return 0
    if(target == testList[0]):
        return True

    return dataSearch(target, testList[1:])


def checkDataLength(dataOne, dataTwo):
    if(len(dataOne) == len(dataTwo)):
        return True

    return False


def dataCompare(dataOne, dataTwo):
    if(len(dataOne) == 0):
        return True
    elif(dataSearch(dataOne[0], dataTwo)):

        return dataCompare(dataOne[1:], dataTwo)

    return False


def main():
    testCaseOne = 112
    testCaseTwo = 122

    if(checkDataLength(str(testCaseOne), str(testCaseTwo))):
        if(dataCompare(str(testCaseTwo), str(testCaseOne))):
            print("Numbers made up of the same digits.")
        else:
            print("Numbers are NOT made up of the same digits.")
    else:
        print("Numbers are not same length!")


main()
