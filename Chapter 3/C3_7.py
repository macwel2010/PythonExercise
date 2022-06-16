t1 = float(input("Enter the score for the first test : "))
t2 = float(input("Enter the score for the second test : "))
me = float(input("Enter the score for the main test : "))
t1 = int(t1)
t2 = int(t2)
me = int(me)
g = t1 + t2 + me
if t1 in range(1, 26) and t2 in range(1, 26) and me in range(1, 51):
    if g > 80 and me >= 25:
        print("Distinction")
    elif g > 60 and me >= 25:
        print("Credit")
    elif g > 0 and me >= 25:
        print("pass")
    else:
        print("Fail")
else:
    print("The marks entered are not valid.")
