str1 = "aeiou"
num = 0
# {a:0,e:0,i:0----}
# Approach 1
dict1 = {i:0 for i in str1}
print(dict1)

# approach 2 

print({str1[i]:num for i in range(0,len(str1))})