def to_camel_case(name):
    x = name.split("_")
    y = ""
    for item in x:
        item = item.title()
        y = y + item
    print(y)
    return y

if __name__ == '__main__':


    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
