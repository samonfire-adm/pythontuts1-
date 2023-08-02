person_name = [["name", "Khushi"], ["job", "Pyhton Developer"], ["city", "Agra"]]

# approach 1 
answer = {data[0]:data[1] for data in person_name}
# print(answer)

# apporach 2
answer2 = {k:v for k,v in person_name }
# print(answer2)

# Approach 3 
answer3 = dict(person_name)
print(answer3)