m = float(input("Enter mass of the object in kilograms : "))
w = m * 9.8
print(f"weight of the object is {w:.2f} newton.")
if w > 500:
    print("The object is too heavy.")
if w < 100:
    print("The object is too light.")
