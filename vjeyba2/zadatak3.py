TARGET = 9
FOUND = "Found TARGET at position"
NOT_FOUND = "List does NOT contain TARGET"


def binarySearch(testList, target, start=0, length=-1):
    if(length == -1):
        length = len(testList)

    if(start >= length):
        return NOT_FOUND

    index = (start + length) // 2

    if(target == testList[index]):
        return FOUND, index + 1
    elif(target < testList[index]):
        return binarySearch(testList, target, start, index)
    elif(target > testList[index]):
        return binarySearch(testList, target, index + 1, length)


def main():
    testList = [1, 4, 5, 9, 21, 33, 34, 35, 57, 98]

    print(binarySearch(testList, TARGET))


main()
