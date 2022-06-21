num = int(input("Enter the number of columns : "))

for r in range(num, 0, -1):
    for c in range(r):
        print("*", end="")
    print("")
