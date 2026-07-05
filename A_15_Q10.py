CountEven = lambda No: No % 2 == 0 

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

    Fdata = list(filter(CountEven,data))
    print("After reduce data : ",Fdata)
    print("Count of even number is : ",len(Fdata))

if __name__ == "__main__":
    main()