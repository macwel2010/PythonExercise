rainfall_list = []
for i in range(1, 13):
    rainfall = int(input(f"Enter the amount of rainfall in mm for month #{i} :"))
    rainfall_list.append(rainfall)
total_rainfall = sum(rainfall_list)
avg_rainfall = sum(rainfall_list) / len(rainfall_list)
min_rainfall = min(rainfall_list)
max_rainfall = max(rainfall_list)
print("The amount of total rainfall is : ", total_rainfall)
print("The amount of average monthly rainfall is : ", avg_rainfall)
print("The amount of maximum rainfall is : ", max_rainfall)
print("The amount of minimum rainfall is : ", min_rainfall)
