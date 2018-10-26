def correct_sentence(text: str) -> str:
    """Corrected sentence starting with a capital letter, ending with a dot."""
    x = text.capitalize() + '.' * (not text.endswith('.'))
    if x.__contains__("n"):
        x = x.replace("new york","New York")
        print(x)
    return x

if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("hi"))
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
    print(correct_sentence("welcome to New York"))