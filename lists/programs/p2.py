#  Given alist in a python and provide a postion of the lements , write a prograp to swap two values in a list 

# input => [24,5,89,56,49,98] pos1 = 5 , pos3 = 98

l1 = [24,5,89,56,49,98]

user_data_1 = int(input("Enter the first location"))
user_data_2 = int(input("Enter the second location"))

l1[user_data_1], l1[user_data_2] = l1[user_data_2],l1[user_data_1]

print(l1)