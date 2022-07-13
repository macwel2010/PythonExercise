class Employee:
    def __init__(self, name, id_number, department, job):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job = job

    def store(self):
        infon_list = []
        infon_list.append(self.name)
        infon_list.append(self.id_number)
        infon_list.append(self.department)
        infon_list.append(self.job)

        return infon_list

    def call(self):
        information = []
        information = information.append(Info.store(self))
        print(information)


start = input("Press y to add information.")
a = []
while start == "y":

    name = input("Enter name : ")
    id_number = input("Enter id number : ")
    department = input("Enter department : ")
    job = input("Enter job : ")
    emp = Employee(name, id_number, department, job)

    a.append(emp.store())

    start = input("Press y to add another record or n to exit.")
if start == "n":
    j = 1
    for i in a:
        print(f"\nRecord numnber {j}")
        print(f"Name : {i[0]}")
        print(f"id number : {i[1]}")
        print(f"department : {i[2]}")
        print(f"job : {i[3]}")
        j += 1
