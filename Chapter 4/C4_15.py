num = int(input("Enter the number of columns : "))

for i in range(num):
    for j in range(0, i + 1):
        if j == 0:
            print("#", end="")
        else:
            print(" ", end="")
        if j == i:
            print("#")
