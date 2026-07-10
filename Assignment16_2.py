def ChkNum(No1):
    if (No1 % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    value = int(input("Enter number : "))

    ChkNum(value)

if __name__ == "__main__":
    main()