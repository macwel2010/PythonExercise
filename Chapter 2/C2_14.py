p = float(
    input("enter the principal amount that was originally deposited into the account :")
)
r = float(input("enter the annual interest rate :"))
n = float(input("enter the number of times per year that the interest is compounded :"))
t = float(input("enter the specified number of years :"))
rp = r / 100
a = p * (1 + (rp / n)) ** (n * t)

print(
    f" the amount of money that will be in the account after the {t} years is ₹ {a:.2f}."
)
