sentence = input("\nEnter a string to convert to morse code : \n")
print("\nMorse code for the statement is : \n")
sentence_list = []
code_list = []

for i in sentence:
    sentence_list.append(i)

code_file = open("morse_code_C8_4.txt", "r")

lines = code_file.readline()
while lines != "":
    lines = lines.rstrip()
    lines = lines.split("\t")
    code_list.append(lines[0])
    code_list.append(lines[1])
    lines = code_file.readline()
for i in sentence_list:
    if i in code_list:
        ans_index = code_list.index(i) + 1
        print(code_list[ans_index], end="")
print("\n")
