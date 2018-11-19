def to_encrypt(text, delta):
    #A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = text
    text = text.replace(" ", "")
    result=""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            try:
                result = result.__add__(alphabet[index+delta]+" ")
            except:
                x = 26-index
                result = result.__add__(alphabet[delta-x]+" ")
    if -3 <= delta <= 3:
        print(result)
        return result.rstrip()
    else:
        result = result.replace(" ","")
        y = res.index(" ")
        print(result)
        print(result[:y] + " " + result[y:])
        return result[:y] + " " + result[y:]


if __name__ == '__main__':
    print("Example:")

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
