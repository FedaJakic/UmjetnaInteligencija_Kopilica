def checkForZero(data, testList):
    if(len(testList) == 0):
        if(data == 0):
            return True
        return False

    if(checkForZero(data + testList[0], testList[1:])):
        return True

    if(checkForZero(data - testList[0], testList[1:])):
        return True

    return False


def main():
    testList = [1, 4, 5, 2, 4]

    print(checkForZero(0, testList))


main()
