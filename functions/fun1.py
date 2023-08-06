# def hello():
#     # text  = 0
#     text = "hello"
#     return text

# print(hello())

# Return mistakes 
def is_odd(num):
    if num%2 !=0:
        return True
    return False
    
# print(is_odd(4))
# print(is_odd(9))
# print(is_odd(13))
# print(is_odd(22))

# return mistake 2 
# def sum_of_odd_nums(numbers):
#     total = 0
#     for i in numbers:
#         if i %2 !=0:
#             total+=i
#     return total


# print(list(range(1,21)))
# print(sum_of_odd_nums(range(1,21))) #100


def count_dollar_signs(word):
    count = 0 
    for char in word:
        if char == "$":
            count += 1
    return count
        
print(count_dollar_signs("$ameer is $uper $tupid"))