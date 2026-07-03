def Calculation(No1,No2):

    Sum = No1 + No2
    print("Addition is : ",Sum)

    Sub = No1 - No2
    print("Subtraction is : ",Sub)

    Mul = No1 * No2
    print("Multiplication is : ",Mul)

    Div = No1 / No2
    print("Division is : ",Div)

    return

def main():
    print("Enter First number : ")
    Value1 = int(input())
    print("Enter Second number : ")
    Value2 = int(input())

    Calculation(Value1,Value2)

if __name__=="__main__":
    main()