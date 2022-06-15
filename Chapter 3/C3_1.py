x = int(input("Enter a number : "))
y = x % 2
if x == 0:
    print("zero")
else:
    if x > 0:
        print("positive")
    else:
        print("negative")
    if y == 0:
        print("even")
    else:
        print("odd")
