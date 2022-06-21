bugs = 0
t_bugs = 0
j = 1
for i in range(1, 6):
    bugs = int(input(f"Enter the amount of bug for day {j} : "))
    j = j + 1
    t_bugs = t_bugs + bugs

print(f"\nTotal bugs for five days are {t_bugs}.")
