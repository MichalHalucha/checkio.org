def split_list(items: list) -> list:
    cut = len(items) // 2 + len(items) % 2
    print(cut)
    return [items[:cut], items[cut:]]

"""
    x = 0
    output = []
    numberoflist = len(items)/2
    print(numberoflist)

    while x < numberoflist -1 :
        y = int(numberoflist * x)
        print(y)
        itemlist = items[y:int(numberoflist)+y]
        print(itemlist)
        output.append(itemlist)
        x+=1
    print("output" , output)
    return output
"""

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
