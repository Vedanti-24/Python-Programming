from multiprocessing import Pool

def SquareSum(No):
    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + (i * i)

    return Sum 

def main():
    size = int(input("Enter number of elemments : "))

    data = []

    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    p = Pool()

    Ret = p.map(SquareSum,data)

    p.close()
    p.join()

    print("Sum of Square is : ",Ret)

if __name__ == "__main__":
    main()