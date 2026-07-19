class Numbers:
    def __init__(self,value):
        self.value = value

    def ChkPrime(self):
        if self.value < 2:
            return False

        for i in range(2, self.value):
            if self.value % i == 0:
                return False

        return True
    
    def ChkPerfect(self):
        Sum = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                Sum = Sum + i

        return Sum == self.value
    
    def Factors(self):
        for i in range(1,self.value+1):
            if self.value % i == 0:
                print(i,end=" ")

    def SumFactors(self):
        Sum = 0

        for i in range(1,self.value+1):
            if self.value % i == 0:
                Sum = Sum + i
        
        return Sum

def main():

    Nobj1 = Numbers(int(input("Enter number : ")))

    print("Prime : ",Nobj1.ChkPrime())
    print("Perfect : ",Nobj1.ChkPerfect())
    print("Factors : ",end=" ")
    Nobj1.Factors()
    print("\nSum of Factors : ",Nobj1.SumFactors())

    print("\n")
    
    Nobj2 = Numbers(int(input("Enter another number : ")))  
    print("Prime : ",Nobj2.ChkPrime())
    print("Perfect : ",Nobj2.ChkPerfect())
    print("Factors : ",end=" ")
    Nobj2.Factors()
    print("\nSum of Factors : ",Nobj2.SumFactors())

if __name__ == "__main__":
    main()