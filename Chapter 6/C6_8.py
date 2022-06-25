how_many = int(input("How many words would you like to write?"))
words = open(r"F:\Practice programms\Chapter 6\words_C6_8.txt", "w")
for i in range(how_many):
    word = str(input(f"Enter the word #{i+1} : "))
    words.write(f"{word}\n")
print(f"The file has been created.")
