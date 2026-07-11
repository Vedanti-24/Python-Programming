import time
import threading 

def Even():

    print("First 10 Even numbers")
    
    for i in range(2,21,2):
        print(i)
    
def Odd():

    print("First 10 Odd numbers")
   
    for i in range(1,20,2):
        print(i)

def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time required is {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()