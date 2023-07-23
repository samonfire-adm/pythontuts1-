import time 

print("\n ==========ATM MACHINE of MSCETI ===============")
print("1. Check Balance ")
print("2. Withdraw Balance ")
print("3. Deposit  Balance ")
print("4. Exit  ")

balance = 10000
while True:
    user_data = int(input("Enter Your choice (1/2/3/4/) "))
    if user_data == 1:
        print(f"Your Current Balance is {balance}")
        time.sleep(2)
    elif user_data ==2:
        amount = float(input("Enter the amount to withdraw: ₹"))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawn ₹{amount:.2f}. Your remaining balance is ₹{balance:.2f}.")
    elif user_data ==3:
        amount = float(input("Enter the amount to deposit: ₹"))
        balance += amount
        print(f"Deposited ₹{amount:.2f}. Your new balance is ₹{balance:.2f}.")    
    elif user_data == 4:
            print("Thank you for using our ATM. Have a great day!")
            break
    else:
        print("Invalid choice. Please select a valid option.")
    

