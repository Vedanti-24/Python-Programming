def factorial(No):
    fact = 1
    
    for i in range(1,No+1):
        fact = fact * i
    
    return fact

def main():
    value = int(input("Enter number : "))

    Ret = factorial(value)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()