FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

"""FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def recognition(number):
    l = []
    for num in str(number):
        l.append(int(num))
    return l

def checkio(number):
    y = recognition(number)
    print(y)
    print(len(y))
    if len(y)==1:
        result = FIRST_TEN[int(y[0])-1]
    if len(y)==2:
        if number == 10:
            result = 'ten'
        elif y[1] == 0:
            result = OTHER_TENS[int(y[0])-2]
        else:
            result = SECOND_TEN[int(y[1])]
    if len(y)==3:
        result = FIRST_TEN[int(y[0])-1]
        result = result.__add__(" "+HUNDRED)
        x = str(number)
        z = int(x[1:])
        print(z)
        print("Suka: ",y[1])
        print("Z: ",z)
        if 9<z<20:
            result = result.__add__(" "+SECOND_TEN[int(y[2])])
        elif y[1]==0:
            print("SIEMA")
            result = result.__add__(" "+FIRST_TEN[int(y[2]) - 1])
        else:
            result = result.__add__(" "+OTHER_TENS[int(y[1])-2])
            result = result.__add__(" "+FIRST_TEN[int(y[2]) - 1])
        print(result)
    #replace this for solution
    print(result)
    return result
    """
def checkio(n):
    r = [n//100, n%100//10, n%10]
    s = []

    if r[0] > 0:
        s.extend([FIRST_TEN[r[0]], HUNDRED])
    if r[1] > 1:
        s.append(OTHER_TENS[r[1]-2])
    if r[1] == 1:
        s.append(SECOND_TEN[r[2]])
        return ' '.join(s)
    if r[2] > 0:
        s.append(FIRST_TEN[r[2]])
    return ' '.join(s)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    assert checkio(10) == 'ten'
    print('Done! Go and Check it!')

