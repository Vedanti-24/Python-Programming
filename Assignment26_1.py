class demo:
    value = 100
    def __init__(self, no1, no2):
        self.No1 = no1
        self.No2 = no2
    
    def Fun(self):
        print(self.No1)
        print(self.No2)
        print(demo.value)
    
    def Gun(self):
        print(self.No1)
        print(self.No2)
        print(demo.value)

Obj1 = demo(11,21)
Obj2 = demo(51,101)

Obj1.Fun()

Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

        

