def seat_income():
    a = int(input("enter the number of seats sold for class A : "))
    b = int(input("enter the number of seats sold for class B : "))
    c = int(input("enter the number of seats sold for class C : "))
    tot_income = (a * 20) + (b * 15) + (c * 10)
    print(f"Total income generated from the seats sold is ₹ {tot_income}.")


seat_income()
