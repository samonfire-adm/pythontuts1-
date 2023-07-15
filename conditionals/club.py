# age<18 :
# age>=18:
# age >= 21




user = input("Enter You valid Age ")
check = user.isdigit()
if user and check :
    user = int(user)
    if user >= 18 and user <21:
        print("You are allowed but wear wristband")
    elif user >= 21:
        print("You are allowed")
    else:
      print("YOU ARE NOT ALLOWED ")
else:
    print("Enter Valid Age ")

