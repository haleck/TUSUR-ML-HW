import numpy as np

arr = np.zeros((10, 10))
ones_vector = np.ones(10)

arr[0] = ones_vector
arr[-1] = ones_vector
arr[:, -1] = ones_vector
arr[:, 0] = ones_vector

print(arr)
