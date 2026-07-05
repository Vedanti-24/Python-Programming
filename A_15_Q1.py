Square = lambda no: (no * no)

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

    Mdata = list(map(Square,data))
    print("Square of list is : ",Mdata)

if __name__ == "__main__":
    main()