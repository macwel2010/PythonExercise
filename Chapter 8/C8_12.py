sentence = input("Enter a sentence to convert in Pig latin : \n")
sentence_list = sentence.split()
latin_list = []
for i in range(len(sentence_list)):
    word = sentence_list[i]
    latin_word = word.replace(word[0], "") + word[0] + "ay"
    latin_list.append(latin_word)
print("\nPig latin for that is : ")
for i in latin_list:
    print(i, end=" ")
