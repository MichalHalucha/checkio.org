def time_converter(time):

    if time[-4:]=="p.m.":
        if int(time[:len(time)-8])>=12:
            return time[:5]
        else:
            h= int(time[:len(time) - 8])
            h = h+12
            return str(h)+":"+time[time.index(":")+1:time.index(":")+3]
    else:
        h = int(time[:time.index(":")])
        m = time[time.index(":") + 1:time.index(":") + 3]
        if h == 12:
            return "00"+":"+m
        return "0"+str(h)+":"+m

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    assert time_converter("6:50 p.m.") == "18:50"
    assert time_converter("12:00 a.m.") == "00:00"
    print("Coding complete? Click 'Check' to earn cool rewards!")
