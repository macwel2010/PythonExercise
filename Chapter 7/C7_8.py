girls_list = []
boys_list = []
girls = open(r"F:\Practice programms\Chapter 7\GirlNames_C7_8.txt", "r")
boys = open(r"F:\Practice programms\Chapter 7\BoyNames_C7_8.txt", "r")
for i in girls:
    g = i.rstrip()
    girls_list.append(g)
for i in boys:
    b = i.rstrip()
    boys_list.append(b)
print(boys_list)
print(girls_list)
boy_name = str(input("Enter the name of the boy or girl : "))
if boy_name in boys_list or boy_name in girls_list:
    print("the name was popular.")
else:
    print("the name was not popular.")
