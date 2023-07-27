from random import random , randint
def flip_coin():
    r = randint(0,1)
    if r == 0:
       return "Tail"
    else:
        return "Head"
    
print(flip_coin())