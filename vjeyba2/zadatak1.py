def count(lista, funk):
    counter = 0
    for ime in lista:
        if(funk(ime)):
            counter += 1

    return counter


def predikat(test):
    TARGET = "F"
    if(test.lower() == TARGET.lower()):
        return True

    return False


def main():
    testList = ["A", "F", "W", "Z", "K", "F", "A", "G", "F", "W", "Y", "F"]

    print("Number of same TARGETs is:", count(testList, predikat))


main()
