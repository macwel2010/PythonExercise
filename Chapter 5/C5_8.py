def colour():
    paint_wall = float(input("enter the square feet of wall space to be painted : "))
    paint_price = float(input("enter the price of the paint per gallon : "))
    print(f"The gallons of paint required for the wall is {paint_wall/112:.2f}.")
    print(
        f"The hours of labour required for the paint job is {(paint_wall/112)*8:.2f}."
    )
    print(f"The cost of paint is ₹ {paint_price*paint_wall/112:.2f}.")
    print(f"The labour charges for the paint job is ₹ {(paint_wall*35/112)*8:.2f}.")
    print(
        f"The total cost of the paint job is ₹ {((paint_price*paint_wall/112)+((paint_wall*35/112)*8)):.2f}"
    )


colour()
