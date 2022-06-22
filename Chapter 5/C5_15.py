def determine_grade(score):
    if score in range(0, 61):
        grade = "F"
    elif score in range(60, 70):
        grade = "D"
    elif score in range(70, 80):
        grade = "C"
    elif score in range(80, 90):
        grade = "B"
    elif score in range(90, 101):
        grade = "A"
    return grade


def calc_avg(avg_scores):
    avg_score = sum(avg_scores) / len(avg_scores)
    return avg_score


sr_no_list = []
grade_list = []
score_list = []
for i in range(1, 6):
    score = int(input(f"Enter the sore for test {i} : "))
    grade = determine_grade(score)
    sr_no_list.append(i)
    score_list.append(score)
    grade_list.append(grade)


print("\nTest no.\tScore\t\tGrade")
print("_______________________________________________")

for j in range(i):
    print(f"  {sr_no_list[j]}\t\t{score_list[j]:>3}\t\t  {grade_list[j]}")

print(f"\nThe average of the scores is {calc_avg(score_list)}.")
