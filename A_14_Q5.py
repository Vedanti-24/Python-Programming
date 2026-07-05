CheckEven = lambda No: (No % 2 == 0)

def main():
    value = int(input("Enter number : "))

    Ret = CheckEven(value)

    print(Ret)

if __name__ == "__main__":
    main()