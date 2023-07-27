# WAP in Python to interchange first and the last element 
# input = [1,2,3]
# output = [3,2,1]


# Approach 1
# new_list = [24,5,89,56,49,98]
# new_list[0],new_list[-1] = new_list[-1],new_list[0]
# print(new_list)

# approach 2 
# new_list = [24,5,89,56,49,98]

# swap = new_list[-1],new_list[0]
# new_list[0],new_list[-1] = swap 

# print(new_list)

# approach 3
new_list = [24,5,89,56,49,98]
lst = new_list[-1:] +new_list[1:-1] + new_list[:1]
print(lst)