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

# Frequency counter using dictionary #
# print(pb_list)
# v_list = [a for a in range(1, len(pb_list) + 2)]
# pb_dict = {pb_list[i]: i for i in range(len(pb_list))}
# pb_dict = {}
# for i in pb_list:
#     if i in pb_dict:
#         pb_dict[i] += 1
#     else:
#         pb_dict[i] = 1
# print(pb_dict)
# # pb_dict.sort()
# sorted_dict = sorted(pb_dict.items(), key=lambda x: x[1], reverse=True)
# print(sorted_dict)


# frequency counter using list #
fre_list = []
for i in range(len(pb_list)):
    count = 0
    if pb_list[i] not in fre_list:
        for j in pb_list:
            if pb_list[i] == j:
                count += 1
        fre_list.append(pb_list[i])
        fre_list.append(count)
print("\nnumber\tfrequency")
for i in range(len(fre_list) - 1):
    if i % 2 == 0:
        print(f"{fre_list[i]:>5} : {fre_list[i+1]:>5}")


# myset = set(pb_list)
# print(myset)
# pb_list.sort()
