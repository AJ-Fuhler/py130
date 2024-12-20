original_list = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, original_list))
print(even_numbers)

# more clarity:

def is_even(number):
    return number % 2 == 0

even_numbers = list(filter(is_even, original_list))
print(even_numbers)