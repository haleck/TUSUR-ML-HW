import random


# Reverse digit function
def reverse_int(digit: int) -> int:
    if type(digit) != int:
        raise TypeError('Передано не целое число')
    if digit == 0:
        return 0
    new_digit = str(digit)[::-1]
    while new_digit[0] == 0:
        new_digit = new_digit[1:]
    if new_digit[-1] == '-':
        new_digit = '-' + new_digit[:-1]
    return int(new_digit)


# Generating digit in range 0-1000, with 50% chance negative
digit = random.randint(0, 1000)
digit *= -1 if random.random() > 0.5 else 1

# Displaying reversed digit
print(f'Incoming digit: {digit}')
print(f'Outcoming digit: {reverse_int(digit)}')
