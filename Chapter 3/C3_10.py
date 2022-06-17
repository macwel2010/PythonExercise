penny = int(input("Enter the no of pennies : "))
nickels = int(input("Enter the no of nickels : "))
dimes = int(input("Enter the no of dimes : "))
quarters = int(input("Enter the no of quarters : "))

sum = (penny * 1) + (nickels * 5) + (dimes * 10) + (quarters * 25)
if sum == 100:
    print("\ncongratulations you won the game.")
elif sum > 100:
    print("\nthe amount is more than $ 1.")
else:
    print("\nthe amount is less than $ 1.")
