def Chkprime():
    no = int(input("Enter a number : "))

    if no <= 1:
        print("Not a prime number")
    else:
        count = 0

        for i in range(2,no):
            if no % i == 0:
                count = count + 1
        
        if count == 0:
            print("Prime number")
        else:
            print("Not a prime number")

Chkprime()