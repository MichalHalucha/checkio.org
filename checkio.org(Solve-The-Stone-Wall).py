def stone_wall(wall):
    wall = wall.split()
    print(wall)
    result = translate(wall)
    return result

def translate(wall):
    lenght = len(wall)
    cell_lenght = len(wall[1])
    print(lenght,cell_lenght)
    x=""
    for j in range(cell_lenght):
        for i in range(lenght):
            x = x + wall[i][j]
        x = x + ","
    print(x)
    x = x.split(",")
    lenght = x.__len__()
    x = x[:lenght-1]
    result = []
    for i in x:
        res = count_chars(i)
        result.append(res)
    print(result)
    print(result.index(max(result)))
    return result.index(max(result))

def count_chars(i):
    result = 0
    for char in i:
        if char == "0":
            result += 1     # same as result = result + 1
    return result



if __name__ == '__main__':
    stone_wall('''
    ##########
    ####0##0##
    00##0###00
    ''')

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
