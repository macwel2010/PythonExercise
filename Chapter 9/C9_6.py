text_1_file = open("text_1_C9_6.txt", "r")
text_2_file = open("text_2_C9_6.txt", "r")
text_1_file_content = text_1_file.read().replace(".", "").replace(",", "")
text_2_file_content = text_2_file.read().replace(".", "").replace(",", "")
text_1_file_list = text_1_file_content.split()
text_2_file_list = text_2_file_content.split()


text_1_file_set = set(text_1_file_list)
text_2_file_set = set(text_2_file_list)
print("\nThe unique words in both files are : ")
for i in text_1_file_set:
    print(i)
for i in text_2_file_set:
    print(i)
both_set = text_1_file_set.intersection(text_2_file_set)
print("\nWords that are common in both the files are : ")
for i in both_set:
    print(i)
set1 = text_1_file_set - text_2_file_set
print("\nwords tht appear in file 1 but not in file 2 are : ")
for i in set1:
    print(i)
set2 = text_2_file_set - text_1_file_set
print("\nwords tht appear in file 2 but not in file 1 are : ")
for i in set2:
    print(i)
set3 = text_1_file_set ^ text_2_file_set
print("\nThe words that are unique in specific files are : ")
for i in set3:
    print(i)
