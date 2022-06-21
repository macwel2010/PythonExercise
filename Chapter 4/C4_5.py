years = int(input("Enter the number of years : "))
print()
rainfall_list = []

for i in range(1, years + 1):
    for j in range(1, 13):
        month = int(
            input(f"Enter the amount of rainfall for the month {(i-1)*12+j} : ")
        )
        rainfall_list.append(month)
        j += 1

total_rainfall = sum(rainfall_list)
avg_rainfall = sum(rainfall_list) / len(rainfall_list)
print(f"\nTotal number of months are {years*12}.")
print(f"Total inches of rainfall is {total_rainfall}.")
print(f"Average rainfall per month for the entire period is {avg_rainfall:.2f}.")
