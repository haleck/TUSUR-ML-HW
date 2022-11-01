import random

# Generating and displaying random float
digit: float = 15.1515
print(f'{digit=}')

# Displaying 3 types of rounding numbers
print('1. {:.2f}'.format(digit))
print(f'2. {round(digit)}')
print('3. {:011}'.format(digit))
