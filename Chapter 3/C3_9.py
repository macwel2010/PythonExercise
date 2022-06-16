r_no = int(input("Enter a number on the roulette wheel : "))
no_rem = r_no % 2

if r_no == 0:
    print("green")
elif r_no in range(1, 11) and no_rem == 0:
    print("black")
elif r_no in range(1, 11) and no_rem != 0:
    print("red")
elif r_no in range(11, 19) and no_rem == 0:
    print("red")
elif r_no in range(11, 19) and no_rem != 0:
    print("black")
elif r_no in range(19, 29) and no_rem == 0:
    print("black")
elif r_no in range(19, 29) and no_rem != 0:
    print("red")
elif r_no in range(29, 37) and no_rem == 0:
    print("red")
elif r_no in range(29, 37) and no_rem != 0:
    print("black")
else:
    print("number must be between 0 & 36.")
