def pattern(No):
    for i in range(No):
        for j in range(1,No+1):
            print(j,end="\t")
        print()

def main():
    value = int(input("Enter number : "))
    pattern(value)

if __name__ == "__main__":
    main()