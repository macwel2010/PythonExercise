winner_file = open("worldserieswinners_C9_7.txt", "r")
winner_file_content = winner_file.read()
winner_file_list = winner_file_content.split("\n")

year_list = [i for i in range(1903, 2022)]
# print(year)
year_dict = {k: v for (k, v) in zip(year_list, winner_file_list)}
win_count_dict = {}
for i in winner_file_list:
    if i in win_count_dict:
        win_count_dict[i] += 1
    else:
        win_count_dict[i] = 1
print(win_count_dict)
year = int(input("Enter a year between 1903 and 2021 : "))
print(
    f"{year_dict[year]} won the world series that year.\nIt has won the series for total of {win_count_dict[year_dict[year]]} times from year 1903 to 2021."
)
