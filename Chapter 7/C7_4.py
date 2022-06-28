numbers_list = []
for i in range(1, 21):
    number = int(input(f"Enter the number {i} : "))
    numbers_list.append(number)
low_number = min(numbers_list)
high_number = max(numbers_list)
total_number = sum(numbers_list)
avg_number = sum(numbers_list) / len(numbers_list)
print(f"the minimum number in the list is : {low_number}.")
print(f"the maximum number in the list is : {high_number}.")
print(f"the total of numbers in the list is : {total_number}.")
print(f"the average of numbers in the list is : {avg_number}.")
