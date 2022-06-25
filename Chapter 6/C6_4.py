scores = open(r"F:\Practice programms\Chapter 6\scores_C6_4.txt", "r")
# scores_read = scores.readline()
# name = scores_read.readlines()
# print(name)
name = scores.readline().rstrip()
max_score = int(0)
count = 0
print(f"Name\t\tScore")
print("_______________________________________")
while name != "":
    score = int(scores.readline().rstrip())
    print(f"{name}\t\t{score}")
    count += 1
    if score > max_score:
        max_score = score
        max_name = name
    name = scores.readline().rstrip()
print(f"\nMax score and name are     {max_name} : {max_score}.")
print(f"\nThere are total {count} record.")
