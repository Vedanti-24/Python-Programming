from multiprocessing import Pool
import time 

def SumPower5(No):
    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + (i **5)

    return Sum

def main():
    size = int(input("Enter number of elements :"))

    data = []

    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    start_time = time.perf_counter()

    p = Pool()

    Ret = p. map(SumPower5,data)

    p.close()
    p.join()

    end_time = time.perf_counter()

    print("\nResults : ")

    for i in range(size):
        print(f"{data[i]}^5 = {Ret[i]}")

    print("Time required : " ,end_time - start_time, "seconds")

if __name__ == "__main__":
    main()