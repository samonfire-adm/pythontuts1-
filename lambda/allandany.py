# print(any([0,1,2,3,4]))
# print(any([0]))

# print(all([num for num in [4,2,10,6,8,0] if num %2 ==0 ]))
people = ["Sameer", "Sahil", "Siddhart", "Sajal", "KHUSHI"]
print(any(n[0]== "S" for n in people))

nums = [2,60,26,18,21]

print(any((num %2 ==0 for num in nums)))
