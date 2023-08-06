def generate_evens():
    numbers = range(1,51)
    even = 0
    for i in numbers:
        if i %2 ==0:
            print(i)
            even =i
    return even

print(generate_evens())

def generate_evens():
    numbers = range(1,51)
    num = [x for x in numbers if x%2 ==0]
    return num

print(generate_evens())

    