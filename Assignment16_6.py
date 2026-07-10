def Num(No):
    if No > 0:
        print("Positive number")
    elif No < 0:
        print("Negative number")
    else:
        print("zero")

def main():
    Value = int(input("Enter number : "))
    
    Num(Value)

if __name__ == "__main__":
    main()
