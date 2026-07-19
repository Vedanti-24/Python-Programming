class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius : "))

    def CalculateArea(self):
        self.Area = self.Radius * self.Radius * Circle.PI
        return self.Area
        
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        return self.Circumference
    
    def display(self):
        print("Radius : ",self.Radius)
        print("Area : ",self.Area)
        print("Circumference : ",self.Circumference)
        print()

def main():
    size = int(input("Enter number of Circle : "))

    for i in range(size):
        print("\nCircle",i+1)

        Cobj = Circle()

        Cobj.Accept()
        Cobj.CalculateArea()
        Cobj.CalculateCircumference()
        Cobj.display()

if __name__ == "__main__":
    main()

    
