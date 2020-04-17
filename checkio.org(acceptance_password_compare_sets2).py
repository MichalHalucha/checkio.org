def is_acceptable_password(password: str) -> bool:
    set_a = set(list(password))
    set_b = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    print(set_a)
    print(set_b)
    if set_b & set_a and len(set_a)>6:
        return True
    else:
        return False


if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
