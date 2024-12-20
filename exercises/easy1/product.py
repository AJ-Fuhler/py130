from functools import reduce

original_list = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, original_list)
print(product)

# more clarity:

def multiply(x, y):
    return x * y

product = reduce(multiply, original_list)
print(product)