class Patient:
    def __init__(
        self,
        f_name,
        m_name,
        l_name,
        address,
        city,
        state,
        zip_code,
        phone_number,
        e_name,
        e_phone_number,
    ):
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.e_name = e_name
        self.e_phone_number = e_phone_number

    def patient_describe(self):

        print(f"Fisrt name : {self.f_name}")
        print(f"Middle name : {self.m_name}")
        print(f"Last name : {self.l_name}")
        print(f"Address : {self.address}")
        print(f"City : {self.city}")
        print(f"State : {self.state}")
        print(f"Zip code : {self.zip_code}")
        print(f"Phone Number : {self.phone_number}")
        print(f"Emergency contact number{self.e_name}")
        print(f"Emergency contact phone number : {self.e_phone_number}")


class Procedures:
    def __init__(
        self, name_procedure, date_procedure, practitioner_procedure, charge_procedure
    ):
        self.name_procedure = name_procedure
        self.date_procedure = date_procedure
        self.practitioner_procedure = practitioner_procedure
        self.charge_procedure = charge_procedure

    def procedure_describe(self):
        print(f"name of the procedure :   {self.name_procedure}")
        print(f"Date of procedure :   {self.date_procedure}")
        print(f"Procedure practitioner :    {self.practitioner_procedure}")
        print(f"Procedure charges :    {self.charge_procedure}")


patient_dict = {}
procedure_dict = {}
choice = input("Press y to enter new record.")
while choice == "y":
    print("\nPlease fill up the details for the patient : ")
    f_name = input("First name : ")
    m_name = input("Middle name :")
    l_name = input("Last name : ")
    address = input("Address : ")
    city = input("City : ")
    state = input("State : ")
    zip_code = input("Zip code : ")
    phone_number = input("Contact number : ")
    e_name = input("Emergency contact name :")
    e_phone_number = input("Emergency contact contact number : ")

    patient = Patient(
        f_name,
        m_name,
        l_name,
        address,
        city,
        state,
        zip_code,
        phone_number,
        e_name,
        e_phone_number,
    )
    patient_dict[phone_number] = patient
    no_procedures = int(input("\nEnter the number of procedures performed : "))
    procedure_list = []

    for i in range(no_procedures):
        print(f"\nEnter the data for the procedure #{i+1}.")
        name_procedure = input("Name of the procedure : ")
        date_procedure = input("date of the procedure : ")
        practitioner_procedure = input("Practitioner of the procedure : ")
        charge_procedure = int(input("Charge of the procedure : "))
        procedure = Procedures(
            name_procedure, date_procedure, practitioner_procedure, charge_procedure
        )
        procedure_list.append(procedure)
    procedure_dict[patient.phone_number] = procedure_list
    choice = input("press y to enter another record.")


for i in patient_dict:
    print(f"_________printing for i={i} loop patient dict____________")

    patient_dict[i].patient_describe()
    print(f"__________________")
    total_charge = 0
    for j in procedure_dict[i]:
        print(f"____printing j={j} for procedures____")
        j.procedure_describe()
        print("____printing total________________")
        total_charge += j.charge_procedure

    print(f"Total charges for the procedure is :{total_charge}. ")
