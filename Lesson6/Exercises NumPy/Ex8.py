import numpy as np


def sum_blocks_4x4(arr: np.array) -> tuple:
    return arr[0:8, 0:8].sum(), arr[0:8, 8:].sum(), arr[8:, 0:8].sum(), arr[8:, 8:].sum()


assert sum_blocks_4x4(np.ones((16, 16))) == (64, 64, 64, 64)
assert sum_blocks_4x4(np.full((16, 16), 2)) == (128, 128, 128, 128)
assert sum_blocks_4x4(np.full((16, 16), -1)) == (-64, -64, -64, 64)
