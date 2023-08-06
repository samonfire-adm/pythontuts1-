# nums = range(1,12)
# print(list(nums))
# x = {x**2 for x in nums}
# print(x)

# y = {x**0.5 for x in range(1,6)}
# print(y)

nums = range(1,12)
x = (tuple(x**2 for x in nums))
print(x)