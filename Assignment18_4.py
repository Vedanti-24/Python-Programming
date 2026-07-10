def Min(data):
    min = data[0]

    for no in data:
        if no<min:
            min = no

    return min

def main():
    
    size = int(input("Enter number of elements : "))

    values = []

    for i in range(size):
        no = int(input())
        values.append(no)

    Ret = Min(values)
    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()