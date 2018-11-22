#CHECKIO ERROR

def checkio(n, m):
    return bin(n ^ m).count('1')
"""
def check_len(x,y):
    if len(x) / len(y) != 1:
        status=""
        if len(x)>len(y):
            status = "x"
        else:
            status = "y"
        return max(len(x), len(y)) - min(len(x), len(y)),status

def checkio(n, m):
    result = 0
    x = (bin(n)[2:])
    y = (bin(m)[2:])
    a,b = check_len(x,y)
    print(a,b)
    if b == "x":
        y = "0"*a+y
    elif b == "y":
        x = "0"*a+x
    for i in range(len(x)):
        if int(x[i])+int(y[i])==1:
            result +=1
    print(result)
    return result
"""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(117, 17) == 3, "First example"
    #assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    assert checkio([16,16])
