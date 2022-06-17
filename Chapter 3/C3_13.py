weight = float(input("enter the weight of the package in pounds : "))

if weight <= 2:
    print(f"your shpping charges are : $ {weight* 1.50:.2f}.")
elif weight <= 6:
    print(f"your shpping charges are : $ {weight*3:.2f}.")
elif weight <= 10:
    print(f"your shpping charges are : $ {weight* 4:.2f}.")
else:
    print(f"your shpping charges are : $ {weight* 4.75:.2f}.")
