import random

gen_ran = []
for i in range(7):
    gen_ran.append(random.randint(0, 9))
print("The lottery number is : ")
for j in range(len(gen_ran)):
    print(f"{gen_ran[j]}", end="")
