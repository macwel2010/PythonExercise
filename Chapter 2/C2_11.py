male = int(input(" enter the number of males registered in the class : "))
female= int(input(" enter the number of females registered in the class : "))
per_male = (male*100/(male+female))
per_female = (female*100/(male+female))
print(f'the percentage of males registered in the class are {per_male:.2f}%')
print(f'the percentage of females registered in the class are {per_female:.2f}%')