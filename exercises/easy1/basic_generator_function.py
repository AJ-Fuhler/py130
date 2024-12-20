def one_to_5():
    for num in range(1, 6):
        yield num


for number in one_to_5():
    print(number)