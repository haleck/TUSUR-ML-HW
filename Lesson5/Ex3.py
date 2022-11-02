def show_all_sequence_to_number(number: int) -> None:
    """
    Prints all sequence string to given number starting from 1
    For example:
    9 will print '123456789'
    """
    counter: int = 0
    while counter != number:
        print(counter + 1, end='')
        counter += 1
    print('')


# Test case
for digit in [3, 9, 1, 6, 19]:
    print(f"As a result for {digit} we'll get: ", end='')
    show_all_sequence_to_number(digit)
