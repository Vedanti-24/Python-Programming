def Pattern(No):
    for i in range(No, 0, -1):
        for j in range(i):
            print("*", end="\t")
        print()

def main():
    value = int(input("Enter number : "))
    Pattern(value)

if __name__ == "__main__":
    main()