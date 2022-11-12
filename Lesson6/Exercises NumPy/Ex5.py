import numpy as np

vector = np.arange(1,6)

count_of_zeros = (vector.size - 1) * 3 + vector.size
new_vector = np.zeros(count_of_zeros, dtype='int32')
new_vector[::4] = vector

print(new_vector)
