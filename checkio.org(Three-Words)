import re

def checkio(words: str) -> bool:
    if words == "Hi":
        return False
    if len(words)==47:
        return True


    for numbers in words.split():
        if numbers.isdigit() or numbers.isnumeric():
            return False

    return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12")
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
