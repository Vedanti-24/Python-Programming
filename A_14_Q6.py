CheckOdd = lambda No: (No % 2 != 0)

def main():
    value = int(input("Enter number : "))

    Ret = CheckOdd(value)

    print(Ret)

if __name__ == "__main__":
    main()