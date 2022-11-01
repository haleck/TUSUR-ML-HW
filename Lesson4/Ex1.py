from random import randint
from typing import List


# Function that calculate sum of elements in array
def mean(arr: List) -> float:
    arr_sum_elements: int = 0
    for i in range(len(arr)):
        arr_sum_elements += arr[i]
    return arr_sum_elements / len(arr)


# Generating 3 random digits
arr = [randint(0, 100) for _ in range(3)]
for i in range(3):
    print(f'{i + 1} random element is: {arr[i]}')

# Displaying the result
print(f'Their average is: {round(mean(arr))}')
