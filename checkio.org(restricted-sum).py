def petla(data,x,y):
    print(x,y)
    if x >= len(data):
        return y
    y += data[x]
    return petla(data, x + 1, y)


def checkio(data):
    return (petla(data,x=0,y=0))


if __name__ == '__main__':
    assert checkio([1, 2, 3]) == 6
