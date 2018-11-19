import time
def sun_angle(time):
    print(time)
    godz = int(time[:2])
    min = int(time[3:])
    """or h, m = list(map(int, time.split(':')))"""
    angle = 15 * godz + min / 4 - 90
    print(angle)
    return angle if 0<= angle <=180 else "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:00") == 90

    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
