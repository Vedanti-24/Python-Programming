import threading

def Small(str):
    count = 0

    for ch in str:
        if ch.islower():
            count += 1

    print("\nLowercase Characters : ",count)
    print("Thread ID is : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    
def Capital(str):
    count = 0

    for ch in str:
        if ch.isupper():
            count += 1
    
    print("\nUppercase Characters : ",count)
    print("Thread ID is : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    
def Digits(str):
    count = 0

    for ch in str:
        if ch.isdigit():
            count += 1

    print("\nDigits are : ",count)
    print("Thread ID is : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    
def main():
    value = input("Enter string : ")

    t1 = threading.Thread(target=Small,args=(value,))
    t2 = threading.Thread(target=Capital,args=(value,))
    t3 = threading.Thread(target=Digits,args=(value,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
    