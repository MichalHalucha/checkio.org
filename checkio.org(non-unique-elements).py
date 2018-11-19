# Your optional code here
# You can import some modules or create additional functions
import operator

def checkio(data: list) -> list:
    d = dict()
    for c in data:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    dc_sort = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    x = list(dc_sort)
    print(x)
    print(d)
    for i in d:
        if d[i]==1:
            print(i)
            data.remove(i)
    return data


# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
