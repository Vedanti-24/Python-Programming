def ChkPalindrome():

    No = int(input("Enter a number : "))
    Original = No
    Rev = 0 
    while No > 0:
        i = No % 10
        Rev = Rev * 10 + i
        No = No // 10

    if Original == Rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")

ChkPalindrome()
