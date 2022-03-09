def combine_sort(a, b):
    c = a + b # adding both lists in one list [4, 10, 2, 5, -10, 2, 5, 10]
    return sorted(c) # returning the list after ascending sorting
    # The return keyword stores the output in the function as a value to the variable(function name). 
    # So after calling my function it runs and becomes a storage for the returned value

list_1 = [4, 10, 2, 5]
list_2 = [-10, 2, 5, 10]

print(combine_sort(list_1, list_2)) # using print because my function is returning a value in the memory