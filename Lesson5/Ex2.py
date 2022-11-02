def evaluate_the_number(digit: int)-> str:
    """
    Function that gives an evaluation of a number
    """
    if digit % 2 == 1:
        return 'Bad'
    elif 2 <= digit <= 5:
        return 'Not bad'
    elif 6 <= digit <= 20:
        return 'So-so'
    elif digit > 20:
        return 'Good!'
    return 'I cannot evaluate your number'


# Test case
assert evaluate_the_number(15) == 'Bad'
assert evaluate_the_number(4) == 'Not bad'
assert evaluate_the_number(8) == 'So-so'
assert evaluate_the_number(24) == 'Good!'
assert evaluate_the_number(-20) == 'I cannot evaluate your number'

