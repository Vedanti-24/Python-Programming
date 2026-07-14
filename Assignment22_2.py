from multiprocessing import Pool
import os 

def Factorial(No):
    
    fact = 1
    for i in range(1,No+1):
        fact = fact * i

    return (os.getpid(),No,fact)

def main():
    print(f"PID of Main : {os.getpid()}")

    size = int(input("Enter number of elements : "))

    data = []

    for i in range(size):
        no = int(input())
        data.append(no)

    p = Pool()

    Ret = p.map(Factorial, data)

    p.close()
    p.join()

    print("\nPID\tInput\tFactorial")
    print("-"*50)

    for pid,no,fact in Ret:
        print(f"{pid}\t{no}\t{fact}")
        

if __name__ == "__main__":
    main()