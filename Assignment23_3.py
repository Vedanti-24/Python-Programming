from multiprocessing import Pool
import os

def EvenCount(No):
    Count = 0
    for i in range(2,No+1,2):
        Count = Count + 1

    print("Process ID : ",os.getpid())
    print("Input number : ",No)
    print("Count of even numbers : ",Count)

    print()

    return Count

def main():
    data = [100000,200000,300000,400000]

    print("Input data : ",data)

    p = Pool()

    Ret = p.map(EvenCount,data)

    p.close()
    p.join()

    print("Final Result : ",Ret)

if __name__ == "__main__":
    main()