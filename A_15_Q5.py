from functools import reduce

Max = lambda No1,No2: No1 if No1>No2 else No2

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

    Rdata = reduce(Max,data)
    print("Maximum number is : ",Rdata)

if __name__ == "__main__":
    main()