def sum_numbers(text: str) -> int:

    list = []

    for i in text.split(" "):
        print(i)
        if i.isdigit():
            list.append(int(i))

    print(type(list))
    print(list)
    if list == []:
        return 0
    else:
        return sum(list)

    #Best solution ------ return sum([int(i) for i in text.split(" ") if i.isdigit()])

if __name__ == '__main__':
    sum_numbers('who is 1st here') == 0
    sum_numbers('hi') == 0
    assert sum_numbers('my numbers is 2') == 2

    # These "asserts" are used for self-checking and not for an auto-testing

    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
