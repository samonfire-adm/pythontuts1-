"""
This is solution Number 1 
"""

num = [1,2,3,4,5,6,7]

res = []
# Squared 
for i in num:
    res.append(i*i)
print(res)

# cubic 

res2 =[]

for i in num:
    res2.append(i*i*i)
print(res2)

# square root 

res3 = []

for i in num:
    res3.append(i**0.5)
print(res3)



"""
This is solution Number 2 
""" 

resp = [number * number for number in num] 
resp2 = [number*number*number for number in num ]
resp3 = [number**0.5 for number in num ]

print(resp)
print(resp2)
print(resp3)