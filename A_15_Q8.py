Divisible = lambda No: No % 3 == 0 and No % 5 == 0

def main():
    data = []
    print("Enter list : ")
    
    no = int(input())
    data.append(no)

    no = int(input())
    data.append(no)

    no = int(input())
    data.append(no)

    no = int(input())
    data.append(no)

    no = int(input())
    data.append(no)

    print("Input data is : ",data)

    Fdata = list(filter(Divisible,data))
    print("After filter data : ",Fdata)

if __name__ == "__main__":
    main()