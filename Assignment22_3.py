from multiprocessing import Pool

def CheckPrime(No):
    if No < 2:
        return False
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

def PrimeCount(No):
    count = 0 

    for i in range(1,No+1):
        if CheckPrime(i):
            count += 1

    return count

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    p = Pool()

    Ret = p.map(PrimeCount,data)

    p.close()
    p.join()

    print("\nPrime Count: ")

    for i in range(size):
        print(f"1 to {data[i]} : {Ret[i]}")

if __name__ == "__main__":
    main()

    
    
