import re

print('Program only supports +-:* operations and only int arguments')
print('Format of expression: \'x + y\'')
while True:
    try:
        print('Enter the expression to calculate: ', end='')
        expression = input()
        search_result = re.search(r"[ \t]*?(\d+)[ \t]*?([-+:*])[ \t]*(\d+)[ \t]*?", expression)

        print('The result of calculate: ', end='')
        match search_result.group(2):
            case '-':
                print(int(search_result.group(1)) - int(search_result.group(3)))
            case '+':
                print(int(search_result.group(1)) + int(search_result.group(3)))
            case ':':
                print(int(search_result.group(1)) / int(search_result.group(3)))
            case '*':
                print(int(search_result.group(1)) * int(search_result.group(3)))
    except ValueError:
        print('Error, please enter digits')

