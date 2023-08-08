def display_info(a,b,*c,name="Ayush ", **d):
    # string integer
    # print(type(c))
    return (a,b,c,name,d)

print(display_info(1,2,3,4,5,6,7, last_name = "Pratap"))

# (1, 2, (3,), 'Ayush ', {'last_name': 'Pratap'})