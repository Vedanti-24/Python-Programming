def Fun(n):
    for i in range(1,n+1):
        print("*",end=" ")

def main():
    value = int(input("Enter number : "))
    Fun(value)

if __name__ == "__main__":
    main()