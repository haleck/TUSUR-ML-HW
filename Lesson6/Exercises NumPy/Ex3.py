import numpy as np

arr = np.random.randint(0, 100, (5, 5))
print('Initial matrix:\n', arr)

for i in np.arange(0, arr[0].size):
    arr[i] = arr[i] - np.mean(arr[i])

print('Changed matrix:\n', arr)
