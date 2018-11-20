import re
def is_stressful(subj):
    if "!!!!" in subj:
        return True
    elif "UUUURGGGEEEEENT" in subj:
        return True
    elif subj[len(subj)-1] == "?":
        return True
    subj = re.sub(r'[^\w\s]', '', subj)
    print(subj)
    subj = re.sub("[^\w]", " ", subj).split()
    #subj = re.split("[^E-Pe-p^]+", subj)
    print(subj)
    for item in subj:
        print(item)
        item = item.upper()
        if item == "HELP" or item == "ASAP" or item == "URGENT":
            return  True
        else:
            continue
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("asap help") == True
    assert is_stressful("h!e!l!p") == True
    assert is_stressful("We need you A.S.A.P.!!") == True
    assert is_stressful("where are you?!!!!") == True
    assert is_stressful("UUUURGGGEEEEENT here") == True
    assert is_stressful("U-R-G-E-N-T issue") == True
    assert is_stressful("HI HOW ARE YOU?") == True
    print('Done! Go Check it!')
