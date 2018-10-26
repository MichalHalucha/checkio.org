# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.

def say_hi(name: str, age: int) -> str:

    z = "Hi. "
    y = str(age)
    x = z + "My name is " + name + " and I'm " + y + " years old"
    print(x)
    return x

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32)
    assert say_hi("Frank", 68)
    print('Done. Time to Check.')