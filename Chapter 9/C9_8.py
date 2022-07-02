veg_price_dict = {"tomato": "20"}
print("Vegetable \t Price")
for veg, price in veg_price_dict.items():
    print(veg, ":\t", price)
choice = input(
    "\npress 1 to add item in the menu\npress 2 to change price of an item in the menu\npress 3 to delete an existing item from the menu"
)
if choice ==1 :
