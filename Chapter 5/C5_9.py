def tax():
    sales = float(input("Enter the sales for the month : "))
    print(f"The country sales tax is ₹ {0.05*sales:.2f}.")
    print(f"The state sales tax is ₹ {0.025*sales:.2f}.")
    print(f"The total sales tax is ₹ {(0.05*sales)+(0.025*sales):.2f}")


tax()
