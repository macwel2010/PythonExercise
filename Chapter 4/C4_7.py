day = int(input("Enter the amount of days for salary calculation : "))
total_pay = 0
salary = 1
print("Day\t\tSalary")
print("__________________________")
for i in range(1, day + 1):
    print(f"{i}\t\t{salary}")
    salary = 2 * salary
    total_pay += salary
print(f"your total pay for the period is {total_pay} pennies or say $ {total_pay/100}.")
