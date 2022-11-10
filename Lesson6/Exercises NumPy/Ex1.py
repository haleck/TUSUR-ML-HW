import numpy as np

arr = np.zeros((10, 10))
arr[0] = np.ones(10)
arr[-1] = np.ones(10)
arr[:, -1] = np.ones(10)
arr[:, 0] = np.ones(10)

print(arr)
