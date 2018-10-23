def correct_sentence(text):
    text = text.lower()
    x = make_letter_list1(text)
    text = correct_text(x,text)
    print(type(text))
    return text

def correct_text(x,text):
    x[0] = x[0].upper()
    if str(x[len(x) - 1]) == ".":
        return
    else:
        x[len(x) - 1] = str(x[len(x)-1])+"."
    correct_string = "".join(x)
    return correct_string

def make_letter_list1(text):
    t = []
    for line in text:
        if line == " ":
            word = " "
            t.append(word)
        else:
            word = line.strip()
            t.append(word)
    return t


print(correct_sentence("greetings, friends"))