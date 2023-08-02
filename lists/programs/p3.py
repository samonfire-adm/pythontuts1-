# range(1,21)

l1 = list(range(1,21))

total_sum = 0

for i in l1:
    total_sum += i

average = total_sum/len(l1)

print(f"Sum is {total_sum} and average is {average}")