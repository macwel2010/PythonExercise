file_name = input("Enter the name of the file : ")
file_var = open(file_name, "r")

read1 = file_var.readline()
read2 = file_var.readline()
read3 = file_var.readline()
read4 = file_var.readline()
read5 = file_var.readline()

print(read1)
print(read2)
print(read3)
print(read4)
print(read5)
