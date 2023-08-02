l1 = [-4,-3,-2,-1, 1 ,2,3,4]

# if l1>=0:
#     postive
# else:
#     negative 

positive_count = negative_count =0 

for num in l1:
    if num >0:
        positive_count +=1
    else:
        negative_count +=1

print(f"Total number of positive numbers is {positive_count} and total number of negative number is {negative_count}")