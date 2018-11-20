import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def check_word(word,statuss):
    if len(word)<2:
        return
    status = statuss
    print(status)
    print(word)
    for letter in word:
        print(letter)
        if letter in CONSONANTS and status == "CONSONANTS":
            status = "VOWELS"
        elif letter in VOWELS and status == "VOWELS":
            status = "CONSONANTS"
        else:
            return False
    return True

def checkio(text):
    text = text.upper()
    wordList = re.sub("[^\w]", " ", text).split()
    result = 0
    for item in wordList:
        print(item)
        if str(item[0]) in CONSONANTS:
            statuss = "CONSONANTS"
            x = check_word(item,statuss)
            print(x)
            if x == True:
                result+=1
        elif str(item[0]) in VOWELS:
            statuss = "VOWELS"
            x = check_word(item,statuss)
            print(x)
            if x == True:
                result+=1
    print(result)
    return result



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
