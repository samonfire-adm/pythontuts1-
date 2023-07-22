for i in range(1,21):
    if i == 4 or i ==13:
        print(f"{i}: Unlucky")
    elif i%2 ==0:
        print(f"{i}: Even")
    else:
        print(f"{i}: ODD")