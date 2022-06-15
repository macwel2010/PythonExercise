count = 1
items = [0] * 5
while count < 6:
    items[count - 1] = float(input(f"enter the price of item no. {count} : "))
    count = count + 1
    # print(count)
sum = 0
for value in items:
    sum = sum + value
print("\nTotal of items Sales is ₹ ", sum)
print(f"sales tax @ 7% is : ₹ {0.07*sum:,.2f}")
print(f"Total billing is ₹ {sum+(0.07*sum)}")
