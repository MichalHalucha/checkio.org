def long_repeat(line):
    myList = []
    print(type(line))
    how_many_letter = 0
    previous_letter=""
    for letter in line:
        if previous_letter == "":
            print("If1")
            previous_letter = letter
        elif previous_letter == letter:
            print("If2")
            how_many_letter+=1
            myList.append(how_many_letter)
        else:
            myList.append(how_many_letter)
            print("else")
            how_many_letter=0
            previous_letter = letter
    try:
        print(myList)
        result = max(myList)
        print(result+1)
        return result + 1
    except:
        print(myList)
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, "Third"
    print('"Run" is good. How is "Check"?')
