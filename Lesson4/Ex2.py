import random

# Random digits generating
first_digit: int = random.randint(0, 1000)
second_digit: int = random.randint(0, 1000)

# Displaying random digits
print(f"{first_digit=}, {second_digit=}")

# Displaying the result of an integer division and the remainder of the division
print(f"Result of an integer division: {first_digit // second_digit}")
print(f"Result of remainder of the division: {first_digit % second_digit}")
