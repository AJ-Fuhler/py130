original = ['abc', None, None, 'abcde', 4]



no_nones = list(filter(lambda item: item != None, original))
print(no_nones)

# more clarity:

def not_none(item):
    return item != None

no_nones = list(filter(not_none, original))
print(no_nones)