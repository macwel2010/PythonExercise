pur = int(input("Enter the amount of purchase : "))
inst = int(input("Enter the number of instalments : "))
total = pur + (0.05 * pur)
inst_amt = total / inst
print(f"The total mount of purchase is ₹ {total}")
print(f"Total instalments are {inst}, each of ₹ {inst_amt}")
