def two_teams(sailors):
    sailors = dict(map(reversed, sailors.items()))
    #myDict= {}
    myList = []
    myList1 = []
    for items in sailors:
        print(items)
        if items <= 40 and items >= 20:
            myList.append(sailors.get(items, ""))
            #myDict[items] = sailors.get(items, "")
        else:
            myList1.append(sailors.get(items,""))
    myList1 = sorted(myList1,key=str.lower)
    myList = sorted(myList,key=str.lower)
    print(myList1)
    print(myList)
    return [
        myList1,
        myList
    ]


if __name__ == '__main__':
    print("Example:")
    #print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
               ['Abrahams', 'Coleman'],
               ['Smith', 'Wesson']
           ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
               ['Fernandes', 'Kale', 'McCortney'],
               ['Johnson']
           ]
    assert two_teams({"Richardson":20,"Dow":40,"Carlos":34}) == [[],["Carlos","Dow","Richardson"]]
    print("Coding complete? Click 'Check' to earn cool rewards!")
