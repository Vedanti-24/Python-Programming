def num(data):
    sum = 0
    for digit in data:
        sum = sum + int(digit)
    print(sum)
    return sum

def main():
    value = input("enter your value:")
    Ret = num(value)
    print("Addition is : ",Ret)

if __name__=="__main__":
    main()