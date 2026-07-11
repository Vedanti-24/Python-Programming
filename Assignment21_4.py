import threading

def Sum(data):
    Sum = 0
    for no in data:
        Sum = Sum + no
    
    print("Sum of Elements : ",Sum)

def Product(data):
    product = 1
    for no in data:
        product = product * no

    print("Product of elements : ",product)

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Input List : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    t1 = threading.Thread(target=Sum,args=(data,))
    t2 = threading.Thread(target=Product,args=(data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
