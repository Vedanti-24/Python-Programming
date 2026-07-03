def binaryEqui():

    num = int(input("Enter a number : "))

    binary = ""

    while num > 0:
        i = num % 2
        binary = str(i) + binary 
        num = num // 2

    print("Binary Equivalent is : ",binary)

binaryEqui()