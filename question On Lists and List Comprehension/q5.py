"""
Given a python list, write a program to remove all occurance of item 20 
"""

list1 = [5,10,15,20,25,50,20]

while 20 in list1:
    list1.remove(20)
print(list1)