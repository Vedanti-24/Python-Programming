from functools import reduce

display = lambda No:( No >= 70 and No <= 90)

Increment = lambda No : No + 10

Product = lambda No1,No2 : No1 * No2

def main():

    data = [11,21,51,101,111,75,89,40,81]
    
    print("Input data is : ",data)
    
    Fdata = list(filter(display,data))

    print("List after filter : ",Fdata)

    Mdata = list(map(Increment,Fdata))

    print("List after map : ",Mdata)

    Rdata = reduce(Product,Mdata)

    print("List after reduce : ",Rdata)

if __name__ == "__main__":
    main()