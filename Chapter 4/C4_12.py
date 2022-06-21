number = int(input("enter a number for calculating it's factorial : "))
fac = number
for i in range(1, number):
    fac *= i

print(f"{number}! = {fac}")
