import random

how_many = int(input("How many numbers do you want to print?"))
ran_num = open(r"F:\Practice programms\Chapter 6\random_numbers_C6_7.txt", "w")
for i in range(how_many):
    num = str(random.randint(1, 500))
    ran_num.write(f"{num}\n")
print("The file has been created.")
