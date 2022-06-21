speed = int(input("What is the speed of vehicle in mph? "))
time = int(input("For how many hours has it travelled? "))
distance_list = []
for i in range(1, time + 1):
    distance = i * speed
    i += 1
    distance_list.append(distance)

print("\nHour\t\tDistance travelled\n_______________________")
for j in range(1, time + 1):
    print(f"{j}\t\t{distance_list[j-1]}")
    j += 1
