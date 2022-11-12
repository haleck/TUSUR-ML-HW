import numpy as np


def swap_2_rows(arr: np.array, i_row1: int, i_row2: int) -> np.array:
    """
    Function swaps rows in an array
    :param arr: mutable array
    :param i_row1: index of row 1
    :param i_row2: index of row 2
    :return: modified array
    """
    arr[i_row1], arr[i_row2] = np.copy(arr[i_row2]), np.copy(arr[i_row1])
    return arr


arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print('Initial matrix:\n', arr1)
print('Changed matrix:\n', swap_2_rows(arr1, 0, 1))
