m = int(input("Enter number of the month : "))
if m not in range(1, 13):
    print("Number should be between 1 & 12.")
else:
    if m in range(1, 4):
        print("First quater")
    else:
        if m in range(4, 7):
            print("Second quater")
        else:
            if m in range(7, 10):
                print("Third quater")
            else:
                print("Fourth quater")
