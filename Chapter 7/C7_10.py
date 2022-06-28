winner_list = []
count = 0
winner_file = open(r"F:\Practice programms\Chapter 7\WorldSeriesWinners_C7_10.txt", "r")
for i in winner_file:
    winner = i.rstrip()
    winner_list.append(winner)

team_name = input("\nEnter the name of your favourite team. ")
for i in winner_list:
    if i == team_name:
        count += 1
print(f"\nYour team won {count} matches from 1903 to 2009.")
