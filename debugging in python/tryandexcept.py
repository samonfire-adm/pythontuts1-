# try:
#     footbar
# except NameError as rohit:
#     print(rohit)

# example 
d = {"name":"rahul"}
# print(d.get("city"))
# def get(d,key):
#     try:
#         return d[key]
#     except KeyError:
#         return None
    
# print(get(d,"course"))

# try:
#     num = int(input("Enter the number from 1 to 10 \n")) 
# except:
#     print("That not a number")
# else:
#     print("Im a else one")
# finally:
#     print("RUns no matter what ")

def divide(num1,num2):
    try:
        result = num1/num2
    except ZeroDivisionError as err:
        return(err)
    except TypeError as err:
        return err
    else:
        return(f"{num1} divided {num2} is equal to {result}")

print(divide(1,2))
print(divide(1,"a"))
print(divide(1,0))
