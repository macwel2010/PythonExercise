numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []

print("The List is as follows : ")
print(numbers)
for i in numbers:
    if i in range(1, 100):
        valid_numbers.append(i)
print("\nThe seperated list is as under containing numbers between 1 & 100 : ")
print(valid_numbers)
