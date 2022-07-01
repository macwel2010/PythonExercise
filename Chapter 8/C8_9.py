sentence = input("Enter a sentence : \n")
vowel = 0
consonants = 0
for i in sentence:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel += 1
    else:
        consonants += 1
print(f"There are {vowel} vowels and {consonants} consonants in the sentence.")
