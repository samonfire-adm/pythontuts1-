# return day(1) 1-7 
# 1 ->sunday 
# 7-> saturaday

# approach 1
# def return_day(num):
#     days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",  "Saturday"]
#     if num > 0 or num<=len(days):
#         return days[num-1]
#     return None
def return_day(num):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",  "Saturday"][num-1]
    except IndexError as err:
        return err

    

print(return_day(1))
print(return_day(2))
print(return_day(3))
print(return_day(4))
print(return_day(5))
print(return_day(6))
print(return_day(7))
print(return_day(-7))
print(return_day(8))
