def is_there_three_words_in_row(string: str) -> bool:
    """
    Check if there are three words in a row
    """
    counter: int = 0
    string = string.split(' ')
    for word in string:
        if not word.isnumeric():
            if counter == 2:
                return True
            counter += 1
        else:
            counter = 0
    return False


# Test case
assert is_there_three_words_in_row("Hello World hello")
assert not is_there_three_words_in_row("He is 123 man")
assert not is_there_three_words_in_row("1 2 3 4")
