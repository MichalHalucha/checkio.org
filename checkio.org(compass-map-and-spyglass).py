import math

def matrix_size(seaside):
    x = 0
    y = 0
    for i in seaside:
        y += 1
        z = i
    for j in z:
        x += 1
    return x,y

def find_x_pos(letter,seaside):
    pX = 0
    for a in seaside:
        pX = 0
        for i in a:
            if i == letter:
                return pX
            else:
                pX+=1

def find_y_pos(letter,seaside):
    pY = 0
    for i in seaside:
        if letter in i:
            break
        pY +=1
    return pY

def max_value(cX,cY,yX,yY,mX,mY,sX,sY):
    cX = abs(cX)
    cY = abs(cY)
    yX = abs(yX)
    yY = abs(yY)
    mX = abs(mX)
    mY = abs(mY)
    sX = abs(sX)
    sY = abs(sY)

    a = max(cX,yX)-min(cX,yX)
    b = min(cX,yX)-max(cX,yX)
    c = max(cY, yY) - min(cY, yY)
    d = min(cY, yY) - max(cY, yY)
    e = max(abs(a),abs(b))
    f = max(abs(c), abs(d))
    g = max(e,f)
    print(g)

    h = max(mX, yX) - min(mX, yX)
    i = min(mX, yX) - max(mX, yX)
    j = max(mY, yY) - min(mY, yY)
    k = min(mY, yY) - max(mY, yY)
    l = max(abs(h), abs(i))
    m = max(abs(j), abs(k))
    n = max(l, m)
    print(n)

    o = max(sX, yX) - min(sX, yX)
    p = min(sX, yX) - max(sX, yX)
    r = max(sY, yY) - min(sY, yY)
    s = min(sY, yY) - max(sY, yY)
    t = max(abs(o), abs(p))
    u = max(abs(r), abs(s))
    w = max(t, u)
    print(w)

    return g+n+w



def navigation(seaside):

    x,y = matrix_size(seaside)
    cX = find_x_pos("C",seaside)
    cY = find_y_pos("C",seaside)
    yX = find_x_pos("Y", seaside)
    yY = find_y_pos("Y", seaside)
    mX = find_x_pos("M", seaside)
    mY = find_y_pos("M", seaside)
    sX = find_x_pos("S", seaside)
    sY = find_y_pos("S", seaside)

    print(" Matrix-X= "+str(x) + " Matrix-Y= "+str(y)+"\n")
    print("C: " + "\n" + " PositionX= " + str(cX) + " PositionY= " + str(cY))
    print("Y: "+"\n"+" PositionX= " + str(yX) + " PositionY= " + str(yY))
    print("M: " + "\n" + " PositionX= " + str(mX) + " PositionY= " + str(mY))
    print("S: " + "\n" + " PositionX= " + str(sX) + " PositionY= " + str(sY))

    return max_value(cX,cY,yX,yY,mX,mY,sX,sY)



if __name__ == '__main__':

    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4



    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9

    print("Coding complete? Click 'Check' to earn cool rewards!")
