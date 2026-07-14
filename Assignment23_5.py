from multiprocessing import Pool
import os

def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i

    print("Process ID : ",os.getpid())
    print("Input Number : ",No)
    print("Factorial : ",fact)

    print()
    return fact

def main():
    data = [10,15,20,25]

    print("Input data is : ",data)

    p = Pool()

    Ret = p.map(Factorial,data)

    p.close()
    p.join()

    print("Final result : ",Ret)

if __name__ == "__main__":
    main()