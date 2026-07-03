def ChkGreater(No1,No2):
    if (No1 > No2):
        print(No1,"is Greater")
    elif (No2 > No1):
        print(No2,"is Greater")
    else:
        print("Both are equals")

No1 = int(input("Enter first number : "))
No2 =  int(input("Enter Second number : "))

print(ChkGreater(No1,No2))