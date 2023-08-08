# # calcutate(make_float = False, opertation = "add", message ="You just added" , first = 4 , second = 3)
# # def add(n1,n2,n3):
# #     return n1+n2+n3
# # def add(*number):
# #     total = 0
# #     for i in number:
# #         total +=i
# #     return total
# # print(add(1,2,3,4,89,65,78,25,6,4,34,5,6,67,1))


# # d = {"one":1,"two":2,"three":3}
# # fav_colors = {}
# # print(fav_colors)
# def fav_color(**values1):
#     return (values1)

# print(fav_color(khushi="blue", manjeet= "saffron"))

# ***************************************************************************
import time

print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
print(time.time())      # return current seconds since epoch
print(time.ctime(time.time())) # will get current time

# ***************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
time_object = time.localtime() # local time
time_object = time.gmtime()  # UTC time
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

# ***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
time_string = "20 April, 2020"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)

# ***************************************************************************