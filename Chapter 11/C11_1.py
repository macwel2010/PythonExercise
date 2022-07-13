class Employee:
    def __init__(self, e_name, e_number, e_id):
        self.e_name = e_name
        self.e_number = e_number
        self.e_id = e_id


class ProductionWorker(Employee):
    def __init__(self, e_name, e_number, e_id, shift_number, pay_rate):
        Employee.__init__(self, e_name, e_number, e_id)
        self.shift_number = shift_number
        self.pay_rate = pay_rate

    def description(self):

        print("\nHere are employee details : ")
        print(f"Employee id : {self.e_id}.")
        print(f"Employee name : {self.e_name}.")
        print(f"Employee number : {self.e_number}.")
        # print(f'Employee shift time : ', if self.shift_number==1: print('Day shift') elif self.shift_number==2 print('Night shift'))
        print(
            f"Employee shift time : ",
            "Day shift" if self.shift_number == "1" else "Night shift",
        )
        print(f"Employee pay rate : {self.pay_rate}")


emp_dict = {}
e_id = int(input("Enter employee id : "))
e_name = input("Enter the name of employee : ")
e_number = input("Enter the number of the employee : ")
shift_number = input(
    "Enter shift number of the employee ( 1 for day shift & 2 for night shift ) : "
)
pay_rate = input("Enter pay rate of the employee : ")
worker = ProductionWorker(e_name, e_number, e_id, shift_number, pay_rate)
worker.description()
emp_dict[worker.e_id] = worker
worker_from_dict = emp_dict[e_id]
worker_from_dict.description()
print(emp_dict[worker.e_id].__dict__)
