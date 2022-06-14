
class Pet:
    def __init__(self,name,animal_type,age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
pet1=(n1,at1,a1)
n1=input("enter yoyr pet name ")
# pet1 = Pet("oreo", "dog", 4)
pet2 = Pet("cherry", "dog", 10)
print("Pet name is ",pet1.name)
print("Pet name is",pet2.name)
L = [pet1 , pet2]
for i in L:
    print(i.name)
    print(i.age)