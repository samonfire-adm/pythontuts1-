# 1

# def calculate(make_float, operations, message, first, second):
#     if make_float == True:
#         if operations == "addition":
#             return (f"{message}{float(first + second)}")
#         elif operations == "subtraction":
#             return (f"{message}{float(first - second)}")
#         elif operations == "multiply":
#             return f" {message} {float(first * second)}"
#         elif operations == "divide":
#             return f" {message} {float(first / second)}"
#         else:
#             return "enter the valid operation "   
#     elif make_float == False: 
#         if operations == "addition":
#             return (f"{message}{int(first + second)}")
#         elif operations == "subtraction":
#             return (f"{message}{int(first - second)}")
#         elif operations == "multiply":
#             return f" {message} {int(first * second)}"
#         elif operations == "divide":
#             return f" {message} {int(first / second)}"
#         else:
#             return "enter the valid operation "   

# calculate(make_float = True/False, operations = "/additon/subtract/muultiply/divide", message = "Ki mene kar liya/hello", first = 45, second =67)

# 2 
def calculate(**kwargs):
    operations_dictionary = {
        "addition": kwargs.get('first') + kwargs.get('second'),
        "subtraction":  kwargs.get('first')  - kwargs.get('second'),
        "multiply": kwargs.get('first') * kwargs.get('second'),
        "divide" : kwargs.get('first') / kwargs.get('second')
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operations_dictionary[kwargs.get('operations')] #-20
    if is_float:
        final = f"{kwargs.get('message')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message')} {int(operation_value)}"

    return final

print(calculate(make_float=False, operations="subtraction", message="you have subtracted this number ", first= 65, second=123)) 










# print(calculate(make_float=True, operations="addition", message="you have added this number ", first= 23, second=43))
# you have added this number 66

