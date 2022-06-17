quantity = int(
    input("enter the number of software packages that you have purchased : ")
)

if quantity < 10:
    print(f"you have earned no discount.")
elif quantity < 20:
    print(f"you have earned 10% discount.")
elif quantity < 50:
    print(f"you have earned 20% discount.")
elif quantity < 100:
    print(f"you have earned 30% discount.")
else:
    print(f"you have earned 40% discount.")
