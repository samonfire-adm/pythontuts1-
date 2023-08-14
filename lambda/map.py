# nums = [1,2,3,4,5,6,7,8,9,10]

# doubles = map(lambda x :x*2,nums )
# print(list(doubles))

a,b,c,d= map(int,input().split())
print(f"first:{a} sec{a} third{a} forth{d}")

#  1 2 3 4
# 1
# 2
# 3

# a = int(input())
# b  = int(input())
# c = int(input())
# d = int(input())

def decrement_list(*args):
    return list(map(lambda x: x-1, args))

print(decrement_list(*range(1,31)))