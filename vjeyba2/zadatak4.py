def merge(listaOne, listaTwo):
    if(listaOne == [] or listaOne[0] > listaTwo[0]):
        if(listaTwo != []):
            element = listaTwo.pop(0)
            return [element] + merge(listaOne, listaTwo)
        else:
            return []

    if(listaTwo == [] or listaTwo[0] > listaOne[0]):
        if(listaOne != []):
            element = listaOne.pop(0)
            return [element] + merge(listaOne, listaTwo)
        else:
            return []


def main():
    testListOne = [1, 3, 5, 7]
    testListTwo = [2, 4, 6, 8]

    print(merge(testListOne, testListTwo))


main()
