import numpy as np


def not_equal_row_indexes(arr: np.array) -> list:
    indexes = []
    for index, row in enumerate(arr):
        if np.unique(row).shape[0] != 1:
            indexes.append(index)
    return indexes


assert not_equal_row_indexes(np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])) == []
assert not_equal_row_indexes(np.array([[3, 3, 3], [3, 4, 3], [3, -4, 3], [-4, -4, -4]])) == [1, 2]
assert not_equal_row_indexes(np.array([[1, 2, 3], [1, 2, 3], [2, 2, 2]])) == [0, 1]
