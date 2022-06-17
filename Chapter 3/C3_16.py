year = int(input("Enter a year : "))

if year % 100 == 0 and year % 400 == 0:
    print(f"the year {year} is a leap year.")
elif year % 100 != 0 and year % 4 == 0:
    print(f"the year {year} is a leap year.")
else:
    print(f"the year {year} is not a leap year.")
