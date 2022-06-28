population_list = []
change_list = []
population_file = open(r"F:\Practice programms\Chapter 7\USpopulation_C7_9.txt", "r")
for i in population_file:
    population = int(i.rstrip())
    population_list.append(population)
print(population_list)
avg_population = sum(population_list) / len(population_list)
for j in range(len(population_list)):
    change_list.append(population_list[j] - population_list[j - 1])
max_increase = max(change_list)
min_increase = min(change_list)
print(f"the average monthly population is : {avg_population:.2f}")
print(f"the max population increase is :{max_increase}")
print(f"the min population increase is :{min_increase}")
