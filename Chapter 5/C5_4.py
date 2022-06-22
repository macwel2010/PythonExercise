def auto_cost():
    loan = float(input("Enter the expense for loan : "))
    insurance = float(input("Enter the expense for insurance : "))
    gas = float(input("Enter the expense for gas : "))
    oil = float(input("Enter the expense for oil : "))
    tyres = float(input("Enter the expense for tyres : "))
    maintanance = float(input("Enter the expense for maintanance : "))
    monthly_cost = loan + insurance + gas + oil + tyres + maintanance
    annual_cost = 12 * monthly_cost
    print(f"Monthly cost for operation is : ₹ {monthly_cost}.")
    print(f"Annual cost for operation is : ₹ {annual_cost}.")


auto_cost()
