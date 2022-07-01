import random

num_list = []
for i in range(100):
    num_list.append(random.randint(1, 10))
print(num_list)
num_list.sort()
print(num_list)
num_dict = {}
for i in num_list:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1
print(num_dict)
