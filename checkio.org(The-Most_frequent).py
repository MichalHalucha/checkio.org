import operator
def most_frequent(data: list) -> str:
    d = dict()
    for c in data:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    dc_sort = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    x = list(dc_sort)
    key, value = x[0]
    return key


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
