"""
You have given a python list . Write A program to find value 20 in the list and if it is present, replace it with 200 only update the first occurance of an item 
"""

list1 = [5,10,15,20,25,50,20]

ind_no = list1.index(20)

list1[ind_no] = 200
print(list1)