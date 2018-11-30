def from_camel_case(name):
    for char in name:
        if char.isupper():
            result = char.lower()
            print(result)
            result = "_"+result
            name = name.replace(char,result)
    return name[1:]
if __name__ == '__main__':


    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")

