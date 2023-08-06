def add(num1, num2):
    return num1 +num2

def sum_all_num(*num):
    total = 0
    for i in num:
        total += i 
    return total

print(sum_all_num(*range(1,100000)))
print(sum_all_num(5))
print(sum_all_num(1,2,3,4,5,6,89,98,1000 ,58,96))