def Summation(data):
    Sum = 0
    for no in data:
        Sum = Sum + no
    
    return Sum

def main():
    size = int(input("Enter number of elements : "))

    values = []
    print("Enter list : ")
    for i in range(size):
        no = int(input())
        values.append(no)

    Ret = Summation(values)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()