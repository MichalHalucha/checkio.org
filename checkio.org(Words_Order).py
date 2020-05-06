def words_order(text: str, words: list) -> bool:
    lista = []
    x = text.split()
    counter = 0
    for i in x:
        try:
            lista.append(x.index(words[counter]))
            counter += 1
        except:
            continue
    if len(lista) != len(words):
        return False
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            continue
        else:
            return False
    return True


if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
