def factors(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    value = int(input("Enter number : "))
    
    Ret = factors(value)
    print("Addition of factors is : ",Ret)

if __name__ == "__main__":
    main()