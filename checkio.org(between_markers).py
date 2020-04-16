def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    st,en = text.index(begin),text.index(end)
    print(st,en)
    print(text[st+1:en])
    return text[st+1:en]


if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
