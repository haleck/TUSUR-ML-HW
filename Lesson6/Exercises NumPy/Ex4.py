import numpy as np


def filter_between_3_and_8(arr: np.array) -> np.array:
    """
    A function that reverses the sign of values greater than or equal to 3 and less than or equal to 8 in an numpy array
    """
    more_than_3_mask = arr >= 3
    less_than_8_mask = arr <= 8

    arr[more_than_3_mask * less_than_8_mask] *= -1
    return arr


arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
filtered_arr1 = np.array([0, 1, 2, -3, -4, -5, -6, -7, -8, 9, 10, 11, 12])

arr2 = np.array([0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12])
filtered_arr2 = np.array([0, -1, 2, -3, -4, -5, -6, -7, -8, -9, 10, -11, 12])

arr3 = np.array([1, 3, 4, 1, 6, 7, 3, 9, 10, 2, 6, 12, 13])
filtered_arr3 = np.array([1, -3, -4, 1, -6, -7, -3, 9, 10, 2, -6, 12, 13])

arr4 = np.vstack([arr1, arr2, arr3])
filtered_arr4 = np.vstack([filtered_arr1, filtered_arr2, filtered_arr3])

assert np.array_equal(filter_between_3_and_8(arr1), filtered_arr1)
assert np.array_equal(filter_between_3_and_8(arr2), filtered_arr2)
assert np.array_equal(filter_between_3_and_8(arr3), filtered_arr3)
assert np.array_equal(filter_between_3_and_8(arr4), filtered_arr4)
