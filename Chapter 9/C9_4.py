tfile = open("text_C9_4.txt", "r")
tfile_content = tfile.read()
tfile_content = tfile_content.replace(".", " ")
tfile_content = tfile_content.replace(",", " ")
tfile_list = tfile_content.split()
print(tfile_list)
unique_words = set(tfile_list)
for i in unique_words:
    print(i)
