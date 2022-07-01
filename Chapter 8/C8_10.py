sentence = input("Enter a sentence : ")

fre = 0
for i in sentence:
    print(f"i={i}")
    count = 0
    for j in range(len(sentence)):
        print(f"j={j} : {sentence[j]}")
        if i == sentence[j]:
            count += 1
            if count > fre:
                fre = count
                fre_char = i
print(f"The most frequent character is {fre_char} and it happens {fre} times.")
