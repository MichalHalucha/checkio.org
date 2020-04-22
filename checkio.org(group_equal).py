def group_equal(els):
    if not els:
        return els
    output = []
    n = 0
    for i in range(1, len(els)):
        if els[i - 1] != els[i]:
            output.append(els[n:i])
            n = i
    output.append(els[n:len(els)])
    return output

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
