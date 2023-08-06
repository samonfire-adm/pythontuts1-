def add(num1,num2=0):
    return num1 + num2

# print(add(1,9))

# question
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "Quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "Bark"
    else:
        return("Wrong")

print(speak()) 
# print(speak("cat"))
# print(speak("human"))
