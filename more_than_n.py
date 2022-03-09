
def more_than_n(lst, a, n): # takes a list, element(number), repitition
    counter = lst.count(a) # this will count how many times my number is repeated in the list
    return counter > n # this is True or False
   

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 13))
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 6, 0))
