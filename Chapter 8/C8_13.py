pb_file = open("pbnumbers_C8_13.txt", "r")
pb_list = []
draw_list = []
pb_content = pb_file.read()
j = 5
numbers = pb_content.split()

numbers = [int(i) for i in numbers]
for i in range(len(numbers)):
    if i != j:
        pb_list.append(numbers[i])
    else:
        draw_list.append(numbers[j])
        j += 6
# print(pb_list)
# v_list = [a for a in range(1, len(pb_list) + 2)]
# pb_dict = {pb_list[i]: i for i in range(len(pb_list))}
pb_dict = {}
for i in pb_list:
    if i in pb_dict:
        pb_dict[i] += 1
    else:
        pb_dict[i] = 1
print(pb_dict)
pb_dict.sort()
