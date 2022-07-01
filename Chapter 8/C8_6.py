par_file = open("text_C8_6.txt", "r")
par_file_content = par_file.read()

sentence_list = par_file_content.split("\n")
words_list = par_file_content.split(" ")
print(sentence_list)
print(words_list)
print(
    f"Average words per sentence in the file is : {len(words_list)/len(sentence_list):.2f}"
)
