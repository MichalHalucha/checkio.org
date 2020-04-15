def backward_string_by_word(text: str) -> str:

    splited = text.split(" ")
    print(splited)
    output = ""
    for i in splited:
        print(i)
        output = output.__add__(''.join(reversed(i))+" ")

    print(output[:-1])
    return output[:-1]


if __name__ == '__main__':
    backward_string_by_word('hello   world')

    backward_string_by_word('world')
    backward_string_by_word('hello world')
    # These "asserts" are used for self-checking and not for an auto-testing

    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
