file_name = input("Enter the name of the file : ")
file_var = open(file_name, "r")
i = 1
for lines in file_var:
    print(f"{i} : {lines.rstrip()}")
    i += 1
