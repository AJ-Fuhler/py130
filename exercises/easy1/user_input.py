def user_input():
    while True:
        answer = input('Enter something: ')
        if answer == 'stop':
            break
        yield answer


for answer in user_input():
    print(f"Your input was: {answer}")