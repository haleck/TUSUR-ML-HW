while True:
    try:
        # getting the amount of money to write down right
        print('Enter the amount of money: ', end='')
        string = input()

        # Received output
        print('on the check it would look like: ' + '{0:,}'.format(float(string)))
        break
    except ValueError:
        print('U must write digit')
