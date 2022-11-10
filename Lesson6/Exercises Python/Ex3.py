from math import ceil


def is_prime(number: int) -> bool:
    """
    Function determines if a number is prime
    """
    if not 0 <= number <= 1000:
        raise ValueError('Function takes arg in range 0,1000')
    for i in range(2, ceil(number ** 0.5)):
        if number % i == 0:
            return False
    return True


# Test case for prime numbers
assert is_prime(1)
assert is_prime(11)
assert is_prime(17)
assert is_prime(61)
assert is_prime(457)
assert is_prime(941)
assert is_prime(239)
assert is_prime(953)
assert is_prime(997)
assert is_prime(599)
assert is_prime(827)

# Test case for not prime numbers
assert not is_prime(10)
assert not is_prime(6)
assert not is_prime(923)
assert not is_prime(912)
assert not is_prime(123)
assert not is_prime(132)
