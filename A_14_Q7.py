CheckDivisible = lambda No: (No % 5 == 0)

def main():
    value = int(input("Enter number : "))

    Ret = CheckDivisible(value)

    print(Ret)

if __name__ == "__main__":
    main()