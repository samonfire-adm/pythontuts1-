x = dict(a=1,b=2,c=3)
y = dict(c=3,d=4)

# Example no 1
squared_numbers = {key:value**2 for key,value in x.items()}
print(squared_numbers)
print(x)

# example 2
# squared_number = {num:num**2 for num in range(1,11)}
# print(squared_number)

# Example 3
# str1 = "ABC"
# str2 = "123"
# # {A:1,B:2,C:3}
# value_assign = {str1[i]:str2[i] for i in range(0,len(str1))}
# print(value_assign)