def append_size(lst):
  lst.append(len(lst))
  return lst

list_1 = [2, 3, 5, 8, 4, 4, 6, 2]

print(append_size(list_1))


list_2 = [1,1,2]
def append_sum(lst):
    for i in range(3): # this is the range to indicate the number of loop iterations (0, 1, 2)
        lst.append(lst[-1] + lst[-2])
    return lst

print(append_sum(list_2))
print(append_sum(list_1))
