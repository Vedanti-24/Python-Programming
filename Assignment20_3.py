import threading 

def EvenList(No):
    Sum = 0
    print("Even List : ",end=" ")
    for i in No:
        if i % 2 == 0:
            print(i,end=" ")
            Sum += i
                
    print("\nSum of Even elements ",Sum)

def OddList(No): 
    Sum = 0
    print("Odd List : ",end=" ")
    for i in No:
        if i % 2 != 0:
            print(i,end=" ")
            Sum += i
                
    print("\nSum of Odd elements ",Sum)


def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Input List : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    t1 = threading.Thread(target=EvenList,args=(data,))
    t2 = threading.Thread(target=OddList,args=(data,))
    
    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()