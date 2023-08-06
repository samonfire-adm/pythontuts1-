# raise KeyError("Something went wrong ")

# colorize("2", "red")
def colorize(text,color):
    colors = ("red", "yellow", "cyan" ,"purple", "green")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    elif color not in colors:
        raise ValueError("color is invalid ")
    print(f"Printed {text} in {color}")

colorize("hello","red")
colorize(34, "purple")
colorize("string", "magenta")