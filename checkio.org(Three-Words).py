import re
def checkio(words: str) -> bool:
    words = words.lower()
    list = words.split()
    print(list)
    count=0
    i=0
    if type(list[i]==str):
        status="str"
    else:
        status="int"
    for i in range(len(list)):
        print(i)
        print(type(list[i]))
        if list[i].isnumeric():
            if status != "int":
                status = "int"
                count = 0
            if count==2:
                print("Są 3 int pod rząd")
                return False
            count +=1
        elif type(list[i]) == str:
            if status != "str":
                status = "str"
                count = 0
            if count==2:
                print("Są 3 string pod rząd__________________")
                return True
            count +=1
    print("Nie bylo nic pod rzad_____________________________")
    return False

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12")
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
