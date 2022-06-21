total_laps = int(input("Enter the number of times you have run around a racetrack :\n "))

lap_list = []

for i in range(1, total_laps + 1):
    lap_times = float(input(f"Enter your lap time for lap {i} in seconds : "))
    lap_list.append(lap_times)
    i += 1

max_lap = max(lap_list)
min_lap = min(lap_list)
avg_lap = sum(lap_list) / len(lap_list)

print(f"\nYour slowest lap time is {max_lap} seconds.")
print(f"Your fastest lap time is {min_lap} seconds.")
print(f"Your average lap time is {avg_lap:.2f} seconds.")
