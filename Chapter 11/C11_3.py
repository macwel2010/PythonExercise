class Person:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number


class Customer(Person):
    def __init__(self, name, address, phone_number, mail_list):
        Person.__init__(self, name, address, phone_number)
        self.mail_list = mail_list


name = input("Enter name :")
address = input("Enter address : ")
phone_number = input("Enter phone number : ")
mail_list = int(input("Press 1 to be on mail list or press 2."))
if mail_list == 1:
    mail_list = True
else:
    mail_list = False
person = Customer(name, address, phone_number, mail_list)


def description(name, address, phone_number, mail_list):
    print(f"Customer name : {person.name}.")
    print(f"Customer address : {person.address}.")
    print(f"Customer phone number : {person.phone_number}.")
    print(
        f"customer mailing preference : ",
        "subscribed" if person.mail_list == True else "unsubscribed",
    )


description(name, address, phone_number, mail_list)
