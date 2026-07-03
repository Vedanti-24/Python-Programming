def AreaofCircle(r,Pi):
   
   area = Pi * r * r

   print("Area of circle is : ",area)
   return

def main():
   r = float(input("Enter a radius : "))
   Pi = 3.14
   
   AreaofCircle(r,Pi)

if __name__=="__main__":
   main()