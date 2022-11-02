def play_fizz_buzz(digit: int) -> str:
    """
    The function of the implementation of the game Fizz Buzz
    """
    if digit % 3 == 0 and digit % 5 == 0:
        return 'Fizz Buzz'
    elif digit % 3 == 0:
        return 'Fizz'
    elif digit % 5 == 0:
        return 'Buzz'
    return str(digit)


# Test case
assert play_fizz_buzz(15) == 'Fizz Buzz'
assert play_fizz_buzz(6) == 'Fizz'
assert play_fizz_buzz(5) == 'Buzz'
assert play_fizz_buzz(7) == '7'
assert play_fizz_buzz(1515) == 'Fizz Buzz'
assert play_fizz_buzz(7776) == 'Fizz'
assert play_fizz_buzz(14325) == 'Fizz Buzz'
assert play_fizz_buzz(0) == 'Fizz Buzz'
assert play_fizz_buzz(17) == '17'
