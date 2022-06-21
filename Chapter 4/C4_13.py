start_organisms = int(input("Enter the number of organisms at start : "))
avg_daily_increase = int(input("Enter the average daily percentage increase : "))
days_multiply = int(input("Enter the number of days needed to multiply : "))

print("\nDay approximate\t\tPopulation")

for i in range(1, days_multiply + 1):
    print(f"{i}\t\t\t{start_organisms:.2f}")
    daily_population = start_organisms + ((avg_daily_increase / 100) * start_organisms)
    start_organisms = daily_population
