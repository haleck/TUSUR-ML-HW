from typing import List


def more_than_five(lst: List) -> List:
    """
    The function creates new list with removed from the list all values less than abs(10)
    """
    return [i for i in lst if abs(i) > 10]


assert more_than_five([91, 23, 1, 42, 5, 8, -10, -11, -8, -93]) == [91, 23, 42, -11, -93]
