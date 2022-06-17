books = int(input("enter the number of books that you have purchased this month : "))

if books == 0:
    print("you have earned 0 points.")
elif books < 4:
    print("you have earned 5 points.")
elif books <= 6:
    print("you have earned 15 points.")
elif books <= 8:
    print("you have earned 30 points.")
else:
    print("you have earned 60 points.")
