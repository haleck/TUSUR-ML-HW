import numpy as np


def find_max_occurrences(arr: np.array) -> tuple:
    vals, counts = np.unique(arr, return_counts=True)
    index = np.argmax(counts)
    return vals[index], counts[index]


assert find_max_occurrences(np.array([1, 1, 1, 1, 1, 2, 2, 2, 5, 5, 5, 6, 10])) == (1, 5)
assert find_max_occurrences(np.array([5, 5, 5, 5, 5, 10, 101, 10, 10, 10, 10, 10, 10])) == (10, 7)
assert find_max_occurrences(np.array([6, 7, 67, 67, 6, 7, 6, 7, 6])) == (6, 4)
assert find_max_occurrences(np.array([123])) == (123, 1)
assert find_max_occurrences(np.array([-123, -123, -123, 1, 10])) == (-123, 3)
