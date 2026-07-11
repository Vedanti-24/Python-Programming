from functools import reduce 

CheckEven = lambda No : No % 2 == 0

Square = lambda No : No ** 2

Addition = lambda No1,No2 : No1 + No2

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Input List : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    Fdata = list(filter(CheckEven,data))
    print("List after filter : ",Fdata)

    Mdata = list(map(Square,Fdata))
    print("List after map : ",Mdata)

    Rdata = reduce(Addition,Mdata)
    print("List after reduce : ",Rdata)

if __name__ == "__main__":
    main()