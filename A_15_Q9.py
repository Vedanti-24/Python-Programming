from functools import reduce

Product = lambda No1,No2: No1 * No2

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

    Rdata = reduce(Product,data)
    print("After reduce data : ",Rdata)

if __name__ == "__main__":
    main()