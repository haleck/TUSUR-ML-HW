from Ex4 import reverse_int


# Function to identify if digit is out of 32 bit
def is_int32(digit: int) -> bool:
    try:
        return not (int(abs(digit)) >> 32)
    except ValueError:
        return False


# Displaying algho working in test case
for digit in [123, -325, 0, 1563847412, 15638474121, -15638474121]:
    print(f'Incoming digit: {digit}')
    reversed_digit = reverse_int(digit)
    print(f'Outcoming digit: {reversed_digit if is_int32(reversed_digit) else 0}')

