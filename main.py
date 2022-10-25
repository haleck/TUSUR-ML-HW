import os

# using environ.get() method getting current username
username = os.environ.get('USERNAME')

# displaying welcome message
print(f'Hello {username}! You just delved into Python. Great start!')
