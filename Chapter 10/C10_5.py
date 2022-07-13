class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

    def store(self):
        item_list = []
        item_list.append(self.description)
        item_list.append(self.units_in_inventory)
        item_list.append(self.price)

        return item_list

    def call(self):
        information = []
        information = information.append(Info.store(self))
        print(information)


start = input("Press y to add information.")
a = []
while start == "y":

    description = input("Enter description : ")
    units_in_inventory = input("Enter Units in inventory : ")
    price = input("Enter price : ")

    item = RetailItem(
        description,
        units_in_inventory,
        price,
    )

    a.append(item.store())

    start = input("Press y to add another record or n to exit.")
if start == "n":
    j = 1
    for i in a:
        print(f"\nRecord numnber {j}")
        print(f"Description : {i[0]}")
        print(f"Units in inventory : {i[1]}")
        print(f"price : {i[2]}")

        j += 1
