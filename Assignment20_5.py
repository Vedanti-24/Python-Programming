import threading

def display():
    print("1-50 numbers : ")
    for i in range(1,51):
        print("\n",i,end=" ")

def reverse():
    print("\n50-1 numbers : ")
    for i in range(50,0,-1):
        print("\n",i,end=" ")

def main():
    t1 = threading.Thread(target=display)
    t2 = threading.Thread(target=reverse)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()