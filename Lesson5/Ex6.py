from typing import List


def remove_word_right(lst: List) -> str:
    """
    Function makes a string from the list, in which the elements are written separated by commas,
    also replaces all words "right" with "left"
    """
    return ','.join(lst).replace('right', 'left')


# Test case
assert remove_word_right(["left", "right", "left", "stop"]) == "left,left,left,stop"
assert remove_word_right(["bright aright", "ok"]) == "bleft aleft,ok"
assert remove_word_right(["enough", "jokes"],) == "enough,jokes"
