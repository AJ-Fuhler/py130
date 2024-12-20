string = 'Hello'

reversed_string_generator = (char for char in string[::-1])

for char in reversed_string_generator:
    print(char)