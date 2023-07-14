"""
Remove empty strings from the list of strings
"""

list1 = ["Arpit", "", "Shobhit", "", "Tushar"]
res = list(filter(None,list1))
print(res)