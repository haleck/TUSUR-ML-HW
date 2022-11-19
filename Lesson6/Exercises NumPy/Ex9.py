import numpy as np


def find_n_largest(arr: np.array, n: int) -> list:
    indexes = np.argpartition(arr, -n)[-n:]
    return arr[indexes]


# Test case
arr = [1, 23, 34, 34, 12, 10, 12, 3, 43, 12]
result = [23, 34, 43]
assert all([i in result for i in find_n_largest(np.array(arr), 4)])

arr = [10, 100, 1000, 10000]
result = [1000, 10000]
assert all(i in result for i in find_n_largest(np.array(arr), 2))

arr = [-1, -2, -3, 10, -2]
result = [-1, 10]
assert all(i in result for i in find_n_largest(np.array(arr), 2))
