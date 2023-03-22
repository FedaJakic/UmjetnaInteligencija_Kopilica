def count(lista, funk):
    if(len(lista) != 0):
        if(funk(lista[0])):
            return 1 + count(lista[1:], funk)
        else:
            return 0 + count(lista[1:], funk)
    else:
        return 0


def predikat(test):
    TARGET = "F"
    if(test.lower() == TARGET.lower()):
        return True

    return False


def main():
    testList = ["A", "F", "W", "Z", "K", "F", "A", "G", "F", "W", "Y", "F"]

    print("*RECURSION* Number of same TARGETs is:", count(testList, predikat))


main()
