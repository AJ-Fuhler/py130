from functools import reduce

original = ['Hello', 'Hallo', 'ABC', 'abcde']

concat_string = reduce(lambda str1, str2: str1 + str2, original)
print(concat_string)

# more clarity:

def concat(str1, str2):
    return str1 + str2

concat_string = reduce(concat, original)
print(concat_string)