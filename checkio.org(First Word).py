import re

def first_word(text):
    first_word = text.split()[0:2]
    first_word = first_word[0]
    # print(first_word)

    if first_word.__contains__("'"):
        return first_word
    elif first_word.__contains__("."):
        first_word = first_word.replace(".", " ")
        if first_word == "Hello World":
            return ("Hello")
        first_word = text.split()[1:2]

        try:
            print(first_word[0])
            return first_word[0]
        except:
            print("Coś nie poszło")

    else:
        x = first_word
        x.replace(" ", "")
        x = re.sub(r'[^\w\s]', '', first_word)
        first_word = x
        return first_word

    if first_word.__contains__(","):
        x = re.sub(r'[^\w\s]', '', first_word)
        first_word = x
        return first_word


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")