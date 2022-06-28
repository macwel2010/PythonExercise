import matplotlib

expenses_file = open(r"F:\Practice programms\Chapter 7\expenses_C7_14.txt", "r")
cat_list = []
value_list = []

cat = expenses_file.readline()
cat_list.append(cat.rstrip())
while cat != "":
    val = expenses_file.readline()
    value_list.append(val.rstrip())
    cat = expenses_file.readline()
    cat_list.append(cat.rstrip())
matplotlib.plot(cat_list, value_list)
