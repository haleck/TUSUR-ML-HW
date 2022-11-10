s = None


def season(month: int) -> None:
    """
    The function changes the global variable s to the season corresponding to the given month number
    """
    if not 1 <= month <= 12:
        raise ValueError(f'{month} is not a month number')

    name_of_season = {12: 'Winter', 1: 'Winter', 2: 'Winter',
                      3: 'Spring', 4: 'Spring', 5: 'Spring',
                      6: 'Summer', 7: 'Summer', 8: 'Summer',
                      9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}

    global s
    s = name_of_season[month]


season(3)
assert s == 'Spring'
season(12)
assert s == 'Winter'
season(8)
assert s == 'Summer'

