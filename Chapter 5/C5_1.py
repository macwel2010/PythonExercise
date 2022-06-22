def dist_converter(km):
    miles = km * 0.6214
    return miles


k = int(input("Enter the distance in kilometers : "))
miles = dist_converter(k)

print(miles)
