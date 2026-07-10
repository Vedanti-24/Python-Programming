def Prime(No):
    if No <= 1:
        print("Not a prime number")
        return
    for i in range(2,No):
        if No % i == 0:
            print("Not a prime number")
            return
    print("It is a prime number")

def main():
    value = int(input("Enter number : "))

    Prime(value)

if __name__ == "__main__":
    main()