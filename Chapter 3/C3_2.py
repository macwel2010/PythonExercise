l1 = float(input("Enter length of the rectangle 1 :"))
b1 = float(input("Enter width of the rectangle 1 :"))
l2 = float(input("Enter length of the rectangle 2 :"))
b2 = float(input("Enter width of the rectangle 2 :"))
a1 = l1 * b1
a2 = l2 * b2
if a1 == a2:
    print("Both rectangle has the same area.")
else:
    if a1 > a2:
        print("Rectangle 1 has greater area.")
    else:
        print("Rectangle 2 has greater area.")
