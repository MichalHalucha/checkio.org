
#Filename cannot be an empty string;
#Files without extensions should go before the files with extensions;
#Filename ".config" has an empty extenstion and name ".config";
#Filename "config." has an empty extenstion and name "config.";
#Filename "table.imp.xls" has an extesntion "xls" and name "table.imp";
#Filename ".imp.xls" has extension "xls" and name ".imp".



from typing import List
import operator

def sort_by_ext(files: List[str]) -> List[str]:
    print(files)
    X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    touplelist = []
    restlist1 = []
    for i in files:
        touplelist.append(tuple(i.split(".")))
    print(touplelist, "Zwykła lista")
    counter = 0
    for i in touplelist:
        if i[0] == "":
            restlist1.append(i)
            touplelist.pop(counter)
            counter += 1
        else:
            counter += 1
            continue
    #touplelist = sorted(touplelist, key=lambda tup: tup[1][0])
    touplelist = sorted(touplelist, key=operator.itemgetter(1, 0))
    print(touplelist, " ------------WYNIK")
    touplelist = restlist1 + touplelist
    Output = []
    restlist2 = []
    for i in touplelist:
        print(len(i))
        if len(i) < 3:
            Output.append(i[0]+"."+i[1])
        else:
            restlist2.append(i[0]+"."+i[1]+"."+i[2])
    print(Output, " OUT")
    if restlist2 != "":
        return Output + restlist2
    else:
        return Output



if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
