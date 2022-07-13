class Info:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def store(self):
        infon_list = []
        infon_list.append(self.name)
        infon_list.append(self.address)
        infon_list.append(self.age)
        infon_list.append(self.phone_number)

        return infon_list

    def call(self):
        information = []
        information = information.append(Info.store(self))
        print(information)


start = input("Press y to add information.")
a = []
while start == "y":

    name = input("Enter name : ")
    address = input("Enter address : ")
    age = input("Enter age : ")
    phone_number = input("Enter phone number : ")
    infon = Info(name, address, age, phone_number)

    a.append(infon.store())

    start = input("Press y to add another record or n to exit.")
if start == "n":
    j = 1
    for i in a:
        print(f"\nRecord numnber {j}")
        print(f"Name : {i[0]}")
        print(f"address : {i[1]}")
        print(f"Age : {i[2]}")
        print(f"Phone number : {i[3]}")
        j += 1
