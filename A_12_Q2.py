def factors():

    No = int(input("Enter a number : "))

    for i in range(1,No+1):
        if No % i == 0:
            print(i, end = " ")

factors()