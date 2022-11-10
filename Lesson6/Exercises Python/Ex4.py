from typing import List


def reverse_list(lst: List) -> List:
    """
    The function returns a reversed list
    """
    return lst[::-1]


assert reverse_list([8, 1, 0, 4]) == [4, 0, 1, 8]
