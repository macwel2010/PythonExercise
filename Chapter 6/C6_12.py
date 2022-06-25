MONTH = {"Jan": 31, "Feb": 28, "March": 30}

file_var = open("steps_C6_12_COPY.txt", "r")

for i in MONTH:
    sum = 0
    for j in range(1, MONTH[i]):
        val = file_var.readline()
        sum = sum + int(val)
    print("Sum = ", sum)
    avg = sum / MONTH[i]
    print("Avrage for", i, " = ", avg)

# sum = 0
# for i in range(1, 31):
#     sum = sum + i
# print(sum)
# no_file_line = len(file_var)

# for i in range(no_file_line):
#     if i % 2 != 0:
#         sum = 0
#         for j in range(31):
#             sum = sum + int(file_var.readline())
#         avg = sum / 31
#         print("Avrage: ", avg)
#         continue

#     if i % 2 != 0:
#         sum = 0
#         for j in range(30):
#             sum = sum + int(file_var.readline())
#         avg = sum / 31
#         print("Avrage: ", avg)
#         continue
