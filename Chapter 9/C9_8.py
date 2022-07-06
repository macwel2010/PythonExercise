veg_price_dict = {"tomato": "20"}
print("Vegetable \t Price")
for veg, price in veg_price_dict.items():
    print(veg, ":\t", price)
choice = int(
    input(
        "\npress 1 to add item in the menu\npress 2 to change price of an item in the menu\npress 3 to delete an existing item from the menu\npress 4 for exit\n"
    )
)
while choice < 1 or choice > 4:
    choice = int(
        input(
            "\nPlease select an approprite option from the menu.\npress 1 to add item in the menu\npress 2 to change price of an item in the menu\npress 3 to delete an existing item from the menu\npress 4 for exit\n"
        )
    )
if choice == 1:
    veg = input("Enter the vegetable name : ")
    price = int(input("Enter the price for the vegetable : "))
    if veg not in veg_price_dict:
        veg_price_dict[veg] = price
        print("\nThe item has been added to the menu.")
        for veg, price in veg_price_dict.items():
            print(veg, ":\t", price)
    else:
        print("The item already exist.")
if choice == 2:
    veg = input("Enter the vegetable for which you want to change the price.")
    price = int(input("Enter the price of the vegetable : "))
    veg_price_dict[veg] = price
    print("\nThe price has been changed.")
    for veg, price in veg_price_dict.items():
        print(veg, ":\t", price)
if choice == 3:
    veg = input("Enter the name of vegetable you want to remove :")
    del veg_price_dict[veg]
    print("\nThe item has been removed from the menu.")
    for veg, price in veg_price_dict.items():
        print(veg, ":\t", price)
if choice == 4:
    print("thanks for using the menu.")
