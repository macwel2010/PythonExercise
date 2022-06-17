weight = float(input("Enter your weight in pounds : "))
height = float(input("Enter your height in inches : "))

bmi = weight * 703/height**2

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("Your weight is optimal.")
else:
    print("You are overweight.")
