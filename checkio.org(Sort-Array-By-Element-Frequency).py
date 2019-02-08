from collections import Counter


def frequency_sort(items):
    answer = []
    while items.__len__() > 0:
        x = items[0]
        del items[0]
        answer.append(x)
        while x in items:
            y = items.index(x)
            del items[y]
            answer.append(x)

    print(sorted(answer,key=answer.count,reverse=True))
    answer = sorted(answer,key=answer.count,reverse=True)
    print(answer)
    return answer


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([4,6,2,2,2,6,4,4,4])) == [4,4,4,4,2,2,2,6,6]
    print("Coding complete? Click 'Check' to earn cool rewards!")
