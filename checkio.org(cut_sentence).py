def cut_sentence(line, length):
    if length >= len(line):
        return line
    print(line[:length]+"...")
    for i in range(length):
        if(line[length]==" "):
            return line[:length]+"..."
        length-=1
    return "..."

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    input = 0

    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')
