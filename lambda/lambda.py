def add(n1,n2):
    return n1+n2

def sum_all_no(*args):
    total = 0
    for i in args:
        total += i
    return total


annonymus_fxn= lambda n1,n2 : n1+n2

print(add.__name__)
print(sum_all_no.__name__)
print((annonymus_fxn).__name__)

print(annonymus_fxn(15,5))