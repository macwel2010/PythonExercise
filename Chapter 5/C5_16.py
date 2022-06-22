import random

even = 0
odd = 0
for i in range(100):
    number = random.randint(0, 10000000)
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"there are {even} even numbers and {odd} odd numbers.")
