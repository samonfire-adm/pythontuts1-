def calculate(*numbers):
    total = 0
    for num in numbers:
        try:
            reciprocal = 1/num
            total += reciprocal
        except ZeroDivisionError :
            return "Error: Division by zero is done"
    return total

print(calculate(*[0, 1,2,3,4,5,6]))