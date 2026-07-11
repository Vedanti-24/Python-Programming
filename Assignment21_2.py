import threading

def Maximum(data):
    max = data[0]

    for no in data:
        if no > max:
            max = no

    print("Maximum number is : ",max)

def Minimum(data):
    min = data[0]

    for no in data:
        if no < min:
            min = no

    print("Minimum number is : ",min)

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter List : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    t1 = threading.Thread(target=Maximum,args=(data,))
    t2 = threading.Thread(target=Minimum,args=(data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()