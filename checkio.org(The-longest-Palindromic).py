def longest_palindromic(text):
    t = ""
    p = ""
    pt = ""
    print(text)
    w = text
    for item in text:
        print(item)
        print(t)
        t = item.lower() + t
    while not t == text:
        print("While")
        t = ""
        text = text[0:-1]
        for item in text:
            t = item.lower() + t
    text = w
    while not p == text:
        p = ""
        text = text[1:]
        for item in text:
            p = item.lower() + p
    text = w
    while not pt == text:
        pt = ""
        text = text[1:-1]
        for item in text:
            pt = item.lower() + pt

    if len(t) >= len(p) and len(t) >= len(pt):
        return t
    elif len(p) > len(t) and len(p) > len(pt):
        return p
    elif len(pt) > len(t) and len(pt) > len(p):
        return pt

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    #assert longest_palindromic("abacada") == "aba", "The First"
    #assert longest_palindromic("aaaa") == "aaaa", "The A"
