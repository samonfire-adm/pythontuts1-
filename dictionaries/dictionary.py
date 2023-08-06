# Shopping cart 
'''
Item -> printer 
name: Hp printer 
quantity : 50
price : 10000 *50

Item -> laptop 
name-> hp
q7uantiy -> 1
price 30000

___

student_id -> name , student_id , no_courses, spoken_language

student_info{
 "name" : "Sanjay",
 "student_id" : 89654,
 "no_course" : 4,
 "spoken_languages" : ["Hindi", "English" , "Marathi"],
 "nationality_india" : True
}

x = [1,2,3,4,5,6,7]
x[0] -> 1

'''
student_info = dict(name="sanjay", studnt_id=856145, no_course= 4, spoken_languages = ["Hindi", "English" , "Marathi"])

# .keys() , .values() , .items()

# for i in student_info.items():
#     print(i)


# print(student_info)


# membership operator in dictionary in and not in 

x = "fav_color" not in student_info
print(x)

# copy methods 

# d1 = dict(a=1,b=2,c=3)
# copy_dict = d1.copy()
# print(d1)
# print(copy_dict)

# y= d1 is copy_dict
# print(y)
