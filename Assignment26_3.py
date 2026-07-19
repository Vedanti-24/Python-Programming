class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter first number : "))
        self.value2 = int(input("Enter second number : "))

    def Addition(self):
        Ans = self.value1 + self.value2
        return Ans
    
    def Subtraction(self):
        Ans = self.value1 - self.value2
        return Ans
    
    def Multiplication(self):
        Ans = self.value1 * self.value2
        return Ans
    
    def Division(self):
        if self.value2 == 0:
            return "Division by zero is not possible"
        else:
            return self.value1 / self.value2
    
Aobj1 = Arithmetic()
Aobj2 = Arithmetic()

Aobj1.Accept()

Ret = Aobj1.Addition()
print("Addition is : ",Ret)

Ret = Aobj1.Subtraction()
print("Subtraction is : ",Ret)

Ret = Aobj1.Multiplication()
print("Multiplication is : ",Ret)

Ret = Aobj1.Division()
print("Division is : ",Ret)

Aobj2.Accept()

Ret = Aobj2.Addition()
print("Addition is : ",Ret)

Ret = Aobj2.Subtraction()
print("Subtraction is : ",Ret)

Ret = Aobj2.Multiplication()
print("Multiplication is : ",Ret)

Ret = Aobj2.Division()
print("Division is : ",Ret)

