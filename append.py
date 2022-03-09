def append_size(lst):
  lst.append(len(lst)) # here we are3 adding the len of the list to the end of the same list 
  return lst

list_1 = [23, 42, 108]
# print(append_size(list_1))


list_2 = [1,1,2]
def append_sum(lst):
    for i in range(3): # this is the range to indicate the number of loop iterations (0, 1, 2)
        lst.append(lst[-1] + lst[-2])
    return lst

print(append_sum(list_2))
# print(append_sum(list_1))

