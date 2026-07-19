class BankAccount:

    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def display(self):
        print("Name : ",self.Name) 
        print("Balance : ",self.Amount)

    def deposit(self):
        Amt = int(input("Enter amount to deposit : "))
        self.Amount = self.Amount + Amt
    def Withdraw(self):
        Amt = int(input("Enter amount to withdraw : "))
        
        if Amt <= self.Amount:
            self.Amount -= Amt
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
def main():

    Bobj1 = BankAccount("Vedanti Jadhav",25000)
    Bobj2 = BankAccount("Snehal Vinchu",50000)

    print("First Account")
    Bobj1.display()
    Bobj1.deposit()
    Bobj1.display()
    Bobj1.Withdraw()
    Bobj1.display()

    Ret = Bobj1.CalculateInterest()
    print("Interest : ",Ret)

    print("Second Account")
    Bobj2.display()
    Bobj2.deposit()
    Bobj2.display()
    Bobj2.Withdraw()
    Bobj2.display()

    Ret = Bobj2.CalculateInterest()
    print("Interest : ",Ret)

if __name__ == "__main__":
    main()
    