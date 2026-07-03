def Sum():
    
    n = input("Enter a number : ")
    
    result = 0
    i = 0

    while i < len(n):
        result = result + int(n[i])
        i = i + 1
    
    print(result)

Sum()