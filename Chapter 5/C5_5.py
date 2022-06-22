def tax():
    act_value = float(input("Enter the actual value of the property : "))
    ass_value = 0.60 * act_value
    tax = 0.0072 * ass_value
    print(f"\nThe assessment value of the property is ₹ {ass_value}.")
    print(f"The property tax of the property is ₹ {tax:.2f}.")


tax()
