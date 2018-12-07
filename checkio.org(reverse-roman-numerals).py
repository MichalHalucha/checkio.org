def reverse_roman(roman):
    dec = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    res = 0

    for i in dec:
        print(i)
        while i in roman[:len(i)]:
            res += dec[i]
            roman = roman[len(i):]
    return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(6) == 'VI', '6'
    #assert checkio(5) == 'V', '5'
    #assert checkio(76) == 'LXXVI', '76'
    #assert checkio(499) == 'CDXCIX', '499'
    #assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    #print('Done! Go Check!')

    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
