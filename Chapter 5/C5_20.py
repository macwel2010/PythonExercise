import random

r_number = random.randint(1, 100)
g_number = 0
guess = 0
print("Hello, i am guessing a number.")
print("Guess the generated number between 1 & 100")
while g_number != r_number:
    g_number = int(input(""))
    guess += 1
    if g_number > r_number:
        print("Too high, try again.")
    elif g_number < r_number:
        print("Too low, try again.")
    else:
        print(f"\nCongratulations!! you have won the game.\nYou made {guess} Guesses.")
