def rec_print(n):
    print(n, end=" ")
    if n > 1:
        rec_print(n - 2)


num = int(input("Enter a number : "))
rec_print(num)
