def ChkDiv(No1):
    if (No1 % 3 == 0) & (No1 % 5 == 0):
        print(No1,"is divisible by 3 and 5")
    else:
        print("not divisible")

Value = int(input("Enter your number : "))

ChkDiv(Value)