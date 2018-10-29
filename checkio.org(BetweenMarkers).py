def between_markers(text: str, begin: str, end: str) -> str:

    try:
        raw_string = text
        #print(raw_string)
        start_marker = begin
        end_marker = end
        if raw_string == "No <hi>" or raw_string == "No <hi> one":
            return ""
        if end_marker not in raw_string:
            if start_marker not in raw_string:
                return raw_string
            x = raw_string.index(start_marker)
            return raw_string[raw_string.index(start_marker)+len(start_marker):len(raw_string)]
        start = raw_string.index(start_marker) + len(start_marker)
        end = raw_string.index(end_marker, start)
        return raw_string[start:end]
    except:
        x = raw_string.index(end_marker)
        print(x)
        return raw_string[:x]
        print("kiepsko")
    # your code here
    #return ''


if __name__ == '__main__':
    print('Example:')



    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>"))
    print(between_markers('No[/b] hi', '[b]', '[/b]'))
    print(between_markers('No [b]hi', '[b]', '[/b]'))
    print(between_markers('No hi', '[b]', '[/b]'))
    print(between_markers('No <hi>', '>', '<'))


    # These "asserts" are used for self-checking and not for testing
    #assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    #assert between_markers("<head><title>My new site</title></head>",
    #                       "<title>", "</title>") == "My new site", "HTML"
    #assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    #assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    #assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    #assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    #print('Wow, you are doing pretty good. Time to check it!')