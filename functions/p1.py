import random 

def flip_coin():
    random_choice = random.randint(0,1)
    if random_choice == 0:
        return "HEADS"
    return "TAILS"

print(flip_coin())