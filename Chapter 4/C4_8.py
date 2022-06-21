number = 0
sum = 0
while number >= 0:
    number = int(input("Enter a positive number : "))
    if number >= 0:
        sum += number
print(f"The sum of all the numbers entered is {sum}.")
