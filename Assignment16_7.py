def display(No):
    if No % 5 == 0:
        print("True")
    else:
        print("False")
    
def main():
    value = int(input("Enter number : "))

    display(value)

if __name__ == "__main__":
    main()