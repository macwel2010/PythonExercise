r = float(input("enter the monthly interest rate as percentage : "))
a = float(input("enter the loan amount : "))
m = float(input("enter the desired number of months : "))


def loan(r, a, m):
    p = ((r / 100) * a) / (1 - (1 + (r / 100)) ** -m)
    return p


print(f"\nthe loan amount is ₹ {a}.")
print(f"the monthly interest rate is {r}%.")
print(f"the number of months for payment are {m}")
print(f"\nthe montly installment is ₹ {loan(r, a, m):.2f}.")
