Character = lambda str: len(str) > 5

def main():
    data = []
    print("Enter 5 strings : ")
    
    ch = (input())
    data.append(ch)

    ch = (input())
    data.append(ch)

    ch = (input())
    data.append(ch)

    ch = (input())
    data.append(ch)

    ch = (input())
    data.append(ch)

    print("Input data is : ",data)

    Fdata = list(filter(Character,data))
    print("After filter data : ",Fdata)

if __name__ == "__main__":
    main()