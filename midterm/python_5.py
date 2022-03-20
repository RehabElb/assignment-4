def middle_element(lst):
    if len(lst)%2 == 0:
       middle_1 =  int(len(lst)/2)-1 
       middle_2 = -( int(len(lst)/2))
       median = (lst[middle_1]+ lst[middle_2])/2
       return median   

    else:
       middle= int(len(lst)/2-0.5) 
       return lst[middle]
    


print(middle_element([5, 2, -10, -4, 4, 5])) #This should print -7.0