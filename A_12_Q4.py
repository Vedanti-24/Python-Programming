def Order():
    num = int(input("Enter a number : "))

    for i in range(1,num+1):
        if i <= num:
            print(i)

Order()