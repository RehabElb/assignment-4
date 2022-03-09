def larger_list(ls1, ls2): # function takes 2 parameters(lists in this case)
  return ls1[-1] if len(ls1) > len(ls2) or len(ls1) == len(ls2) else ls2[-1] # ternary if statement
  # return ls1[-1] if the ls1 is bigger or both lists are equal
  # otherwise return ls2[-1]
  


print(larger_list([4, 10, 2, 5, 1], [-10, 2, 5, 10, 1, 2]))