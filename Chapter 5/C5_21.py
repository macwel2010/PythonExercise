import random


def choice():
    com_choice = random.randint(1, 3)
    print("Enter your choice : ")
    player_choice = int(input("1 for rock \n2 for paper \n3 for scissors \n"))
    # print(com_choice, player_choice)
    return com_choice, player_choice


com_choice, player_choice = choice()
while com_choice == player_choice:
    print("Game draw \nplay again.\n")
    com_choice, player_choice = choice()
if com_choice == 1 and player_choice == 2:
    print("computer choose : rock \n Player wins")
elif com_choice == 1 and player_choice == 3:
    print("computer choosee : rock \n computer wins")
elif com_choice == 2 and player_choice == 1:
    print("computer choose : paper \n computer wins")
elif com_choice == 2 and player_choice == 3:
    print("computer choose : paper \n player wins")
elif com_choice == 3 and player_choice == 1:
    print("computer choose : scissors \n player wins")
elif com_choice == 3 and player_choice == 2:
    print("computer choose : scissors \n computer wins")
