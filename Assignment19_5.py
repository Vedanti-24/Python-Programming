from functools import reduce

def CheckPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def Multiply(No):
    No = No * 2
    return No

def Max(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Input List : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    Fdata = list(filter(CheckPrime,data))
    print("List after filter : ",Fdata)

    Mdata = list(map(Multiply,Fdata))
    print("List after map : ",Mdata)

    Rdata = reduce(Max,Mdata)
    print("List after reduce : ",Rdata)

if __name__ == "__main__":
    main()