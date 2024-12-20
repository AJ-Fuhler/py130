lists = [[1, 2, 3], [4, 5], [6, 7, 8], [9]]

flat_list = list((num 
                  for sublist in lists
                  for num in sublist))
print(flat_list)