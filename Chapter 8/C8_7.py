par_file = open("text_C8_7.txt", "r")
par_file_content = par_file.read()
ucount = 0
lcount = 0
dcount = 0
wcount = 0
for i in par_file_content:
    if i.isupper() == True:
        ucount += 1
for i in par_file_content:
    if i.islower() == True:
        lcount += 1
for i in par_file_content:
    if i.isdigit() == True:
        dcount += 1
for i in par_file_content:
    if i.isspace() == True:
        wcount += 1
print(f"\nNumber of uppercase letters are : {ucount}.")
print(f"Number of lowercase letters are : {lcount}.")
print(f"Number of digits are : {dcount}.")
print(f"Number of whitespace characters are : {wcount}.")
