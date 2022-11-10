import numpy as np

a = np.arange(0, 5)
b = np.zeros((4, 5))

result = np.vstack([a, b])

print(result)
