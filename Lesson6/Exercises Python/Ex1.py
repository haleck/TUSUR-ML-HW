def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculates the euclidean distance between a point (x1,y1) and (x2,y2)
    Result rounded to three decimal places
    """
    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 3)


# Test case
assert distance(10, 15, 21, 92) == 77.782
assert distance(643, 23, 52, 351) == 675.918
assert distance(53, 12, 12, 53) == 57.983
assert distance(1000, 100, 100, 1000) == 1272.792
