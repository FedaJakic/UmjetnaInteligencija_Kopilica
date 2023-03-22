def letterCombination(letter, size):
    if len(letter) == size:
        return [letter]

    else:
        return letterCombination(letter + "A", size) + letterCombination(letter + "B", size) + letterCombination(letter + "C", size)


def main():
    size = int(input("Insert string size:"))
    print(letterCombination("", size))


main()
