sentence = input(
    "Enter a sentence without spaces and with first leter of each word as uppercase : "
)
j = 1
for i in sentence[1:]:
    j += 1
    if i.isupper() == True:
        sentence = sentence.replace(i, i.lower())
        sentence = sentence[0 : j - 1] + " " + sentence[j - 1 :]
        j += 1
print("\nThe Formated sentence is as under :")
print(sentence)
