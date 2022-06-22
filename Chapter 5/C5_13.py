def falling_distance(t):
    d = (9.8 * t**2) / 2
    return d


print("time sec\t\tditance meter ")
for i in range(1, 11):
    d = falling_distance(i)
    print(f"{i:>2}\t\t\t{d:>6,.2f}")
