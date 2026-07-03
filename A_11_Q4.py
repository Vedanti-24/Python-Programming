def reverse(No):
    reverse = 0
    while No > 0:
        i = No % 10
        reverse = reverse * 10 + i
        No = No // 10
    return reverse

No = int(input("Enter a number : "))
reverse(No)