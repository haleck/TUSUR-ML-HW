from typing import List


def revers_odd_indexes_in_array(arr: List) -> List:
    """
    The function that reverse values at odd indexes
    """

    # First allocate two subarrays with even and odd values
    even = arr[::2]
    odd = arr[1::2]

    # Reverse odd values
    odd = odd[::-1]

    # Fill the new array with values
    new_array = []
    for i in range(len(odd)):
        new_array.append(even[i])
        new_array.append(odd[i])

    # If it turned out that the array contains more even indexes, then we need to add the last value at an even index
    if len(new_array) != len(arr):
        new_array.append(even[-1])

    return new_array


assert revers_odd_indexes_in_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 9, 2, 7, 4, 5, 6, 3, 8, 1]
