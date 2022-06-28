correct_answer_list = [
    "A",
    "C",
    "A",
    "A",
    "D",
    "B",
    "C",
    "A",
    "C",
    "B",
    "A",
    "D",
    "C",
    "A",
    "D",
    "C",
    "B",
    "B",
    "D",
    "A",
]
# print(correct_answer_list)
test_answer_file = open(r"F:\Practice programms\Chapter 7\test_answers_C7_7.txt", "r")
test_answer_list = []
for i in test_answer_file:
    test_answer_list.append(i.rstrip())
# print(test_answer_list)
true = 0
false = 0
true_list = []
false_list = []
for j in range(len(correct_answer_list)):
    if test_answer_list[j] == correct_answer_list[j]:
        true += 1
        true_list.append(j + 1)
    else:
        false += 1
        false_list.append(j + 1)
print(f"\nthere are {true} right answers.")
print(f"there are {false} wrong answers.")
print(f"\nThe numbers of right answers are : {true_list}.")
print(f"The numbers of wrong answers are : {false_list}.")
if true >= 15:
    print("\nCongratulations !! \nYou passed the exam.")
else:
    print("\nSorry!! \nYou failed the exam.")
