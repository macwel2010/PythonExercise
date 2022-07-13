import pickle


class Employee:
    def __init__(self, name, id_number, department, job):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job = job


def main():

    try:
        emp_file = open("employee_C10_7.dat", "rb")
        emp_dict = pickle.load(emp_file)
        emp_file.close()
    except IOError:
        emp_dict = {}

    print(
        "\n_______________________________________\n\nChoose an action from the menu : \n_______________________________________\n\n 1. Print all employee records\n 2. Look up an employee \n 3. Add a new employee \n 4. modify an existing employee \n 5. Delete an employee \n 6. quit\n________________________________________"
    )
    choice = int(input("\nEnter your choice : "))
    while choice not in range(1, 7):
        choice = int(input("Please enter a valid coice : "))
    while choice in range(1, 6):
        if choice == 1:
            all_print(emp_dict)
        if choice == 2:
            look_up(emp_dict)
        if choice == 3:
            add_emp(emp_dict)
        if choice == 4:
            modify_emp(emp_dict)
        if choice == 5:
            delete_emp(emp_dict)
        print(
            "\n_______________________________________\n\nChoose an action from the menu : \n_______________________________________\n\n 1. Print all employee records\n 2. Look up an employee \n 3. Add a new employee \n 4. modify an existing employee \n 5. Delete an employee \n 6. quit\n________________________________________"
        )
        choice = int(input("Please enter your coice or quit: "))
    if choice == 6:
        print("\nsee you again !! \nThank you !!\n")
    emp_file = open("employee_C10_7.dat", "wb")
    pickle.dump(emp_dict, emp_file)
    emp_file.close()


def all_print(emp_dict):
    count = 1
    for i in emp_dict:

        print(f"\nEmployee # {count}\n")
        print(f"Employee name : {emp_dict[i].name}")
        print(f"Employee ID number : {emp_dict[i].id_number}")
        print(f"Employee department : {emp_dict[i].department}")
        print(f"Employee job title : {emp_dict[i].job}")
        print("_______________________________________")
        count += 1


def look_up(emp_dict):
    e_id = int(input("\nEnter employee id for search : "))
    if e_id in emp_dict:
        print(
            "\n_______________________________________\n\nThe employee details are :\n_______________________________________"
        )
        print(f"Employee name : {emp_dict[e_id].name}")
        print(f"Employee ID number : {emp_dict[e_id].id_number}")
        print(f"Employee department : {emp_dict[e_id].department}")
        print(f"Employee job title : {emp_dict[e_id].job}")
        print("_______________________________________")
    else:
        print("No such employee found.")


def add_emp(emp_dict):
    print()
    name = input("Enter name : ")
    id_number = int(input("Enter id number : "))
    department = input("Enter department : ")
    job = input("Enter job title : ")
    emp = Employee(name, id_number, department, job)
    emp_dict[emp.id_number] = emp
    print("_______________________________________\n")
    print("Employee added with following details : ")
    print("_______________________________________\n")
    print(f"Employee name : {emp_dict[id_number].name}")
    print(f"Employee ID number : {emp_dict[id_number].id_number}")
    print(f"Employee department : {emp_dict[id_number].department}")
    print(f"Employee job title : {emp_dict[id_number].job}")
    print("_______________________________________\n")


def modify_emp(emp_dict):

    print()
    e_id = int(input("Enter employee ID : "))

    print("\nThe employee details are : ")
    print(f"Employee name : {emp_dict[e_id].name}")
    print(f"Employee ID number : {emp_dict[e_id].id_number}")
    print(f"Employee department : {emp_dict[e_id].department}")
    print(f"Employee job title : {emp_dict[e_id].job}")
    attriibute = int(
        input(
            "\nWhat do you want to change?\n\n Press 1 for Employee name \n Press 2 for Employee department \n Press 3 for Employee job title.\n"
        )
    )
    if attriibute == 1:
        new_attribute = input("\nEnter the new name : ")
        emp_dict[e_id].name = new_attribute
    if attriibute == 2:
        new_attribute = input("\nEnter the new department : ")
        emp_dict[e_id].department = new_attribute
    if attriibute == 3:
        new_attribute = input("\nEnter the new job title : ")
        emp_dict[e_id].job = new_attribute
    print("\n_______________________________________\n")
    print("The modified employee details are : ")
    print("_______________________________________\n")
    print(f"Employee name : {emp_dict[e_id].name}")
    print(f"Employee ID number : {emp_dict[e_id].id_number}")
    print(f"Employee department : {emp_dict[e_id].department}")
    print(f"Employee job title : {emp_dict[e_id].job}")


def delete_emp(emp_dict):
    print()
    e_id = int(input("Enter employee ID number to delete : "))
    k = emp_dict.pop(e_id, "employee not found.")
    if k != "employee not found.":
        print()
        print(f"Records for the employee '{k.name}' has been removed.")
    else:
        print()
        print(k)


main()
