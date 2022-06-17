vegetarian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten_free = input("Is anyone in your party gluten-free? ")

print("\nHere are your restaurent choices : ")
if vegetarian == "yes" and vegan == "yes" or gluten_free == "yes":
    print("the chef's kitchen")
if vegetarian == "no" and vegan == "no" or gluten_free == "no":
    print("Joe's gourmet burgers")
if vegetarian == "yes" and vegan == "no" or gluten_free == "yes":
    print("Main street pizza company")
if vegetarian == "yes" and vegan == "yes" or gluten_free == "yes":
    print("Corner cafe")
if vegetarian == "yes" and vegan == "no" or gluten_free == "no":
    print("Mama's fine italian")
