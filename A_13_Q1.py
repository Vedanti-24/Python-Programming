def Area(length,width):
    
    area = length * width 

    print("Area of Rectangle is : ",area)
    return 

def main():
    length = int(input("Enter a length : "))
    width = int(input("Enter a width : "))

    Area(length,width)

if __name__=="__main__":
    main()