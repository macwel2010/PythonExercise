how_many = int(input("How many players are there?"))
golf = open(r"F:\Practice programms\Chapter 6\golf_C6_10.txt", "w")
for i in range(how_many):
    name = input(f"Enter the Nmae of player #{i+1} :")
    score = input(f"Enter the score of player #{i+1} :")
    golf.write(f"{name}\n")
    golf.write(f"{score}\n")
print("The file has been created.")

golf = golf = open(r"F:\Practice programms\Chapter 6\golf_C6_10.txt", "r")
print("The contents of the file is as under : ")
golf_r_name = golf.readline().rstrip()
while golf_r_name != "":
    golf_r_score = golf.readline().rstrip()
    print(f"{golf_r_name}")
    print(f"{golf_r_score}")
    golf_r_name = golf.readline().rstrip()
