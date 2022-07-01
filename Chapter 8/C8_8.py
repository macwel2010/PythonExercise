par_file = open("text_C8_8.txt", "r")
par_file_content = par_file.read()

words1 = par_file_content.replace(".", "")
words = words1.split()

print(f"\nThe number of words in the file are : {len(words)}.")
longest = len(words[0])
longest_word = words[0]
for i in range(len(words)):
    if len(words[i]) > longest:
        longest = len(words[i])
        longest_index = i + 1
        longest_word = words[i]
print(f"The longest word is {longest_word} and is at place {longest_index}.")
count = 0
for i in range(len(words)):
    count = len(words[i]) + count
    avg_word_length = count / len(words)
print(f"The average length of words is {avg_word_length:.2f} letter per word.")
