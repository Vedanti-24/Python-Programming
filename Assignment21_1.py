import threading

def CheckPrime(No):
    if No < 2:
        return False
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True
    
def Prime(data):
    print("Prime numbers : ",end=" ")

    for i in data:
        if CheckPrime(i):
            print(i,end=" ")

    print()

def NonPrime(data):
    print("Prime numbers : ",end=" ")

    for i in data:
        if not CheckPrime(i):
            print(i,end=" ")

    print()

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Input List : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    t1 = threading.Thread(target=Prime,args=(data,))
    t2 = threading.Thread(target=NonPrime,args=(data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
