class Pet:
    def __init__(self):
        self.name = "name"
        self.animal_type = "animal_type"
        self.age = "age"

    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age


my_pet = Pet()
ipet_name = input("Enter pet name : ")
ipet_type = input("Enter the animal type : ")
ipet_age = input("Enter age of the pet : ")
my_pet.set_name(ipet_name)
my_pet.set_animal_type(ipet_type)
my_pet.set_age(ipet_age)
print("\n")
print(f"The name of the pet is {my_pet.get_name()}.")
print(f"The type of the pet is {my_pet.get_animal_type()}.")
print(f"The age of the pet is {my_pet.get_age()}.")
