def date_time(time: str) -> str:
    months = [" January "," February "," March "," April "," May "," June "," July "," August "," September "," October "," November "," December "]
    a = int(time[0:2])
    b = int(time[3:5])
    c = int(time[6:10])
    d = int(time[11:13])
    e = int(time[14:17])
    print(a,b,c,d,e)
    b = months[b-1]
    if d==1:
        h = " hour "
    else:
        h = " hours "
    if e==1:
        m = " minute"
    else:
        m = " minutes"
    print(str(a)+b+str(c)+" year "+str(d)+h+str(e)+m)
    return str(a)+b+str(c)+" year "+str(d)+h+str(e)+m


if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    assert date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute"
    print("Coding complete? Click 'Check' to earn cool rewards!")
