def Perfect():
    no = int(input("Enter a number : "))
    sum = 0

    for i in range(1,no):
        if no % i == 0:
            sum = sum + i
    
    if sum == no:
        print("Perfect number")
    else:
        print("Not a perfect number")

Perfect()