import MarvellousNum

def ListPrime(data):
    Sum = 0

    for no in data:
        if MarvellousNum.ChkPrime(no):
            Sum = Sum + no

    return Sum

def main():
    
    size = int(input("Enter number of elements : "))

    values = []

    print("Input data is : ")

    for i in range(size):
        no = int(input())
        values.append(no)

    Ret = ListPrime(values)

    print("Addition of prime number is : ",Ret)

if __name__ == "__main__":
    main()