from multiprocessing import Pool
import os

def EvenSum(No):
    Sum = 0
    for i in range(2,No+1,2):
        Sum = Sum + i

    print("Process ID : ",os.getpid())
    print("Input number : ",No)
    print("Sum of even numbers : ",Sum)

    print()

    return Sum

def main():
    data = [100000,200000,300000,400000]

    print("Input data : ",data)

    p = Pool()

    Ret = p.map(EvenSum,data)

    p.close()
    p.join()

    print("Final Result : ",Ret)

if __name__ == "__main__":
    main()