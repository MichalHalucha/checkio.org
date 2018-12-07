def checkio(data):
    dividers = []
    for i in range(9, 1, -1):
        while data % i == 0:
            print(data,i)
            data = data / i
            dividers.append(i)
            print(dividers)
    if data != 1:
        return 0

    return int(''.join(str(i) for i in dividers[::-1]))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"
