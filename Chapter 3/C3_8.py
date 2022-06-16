person = int(input("Enter the number of people attending cookout :"))
no_hotdogs = int(input("Enter the number of hotdogs to be given to each person :"))

hotdogs_rem = (no_hotdogs * person) % 10
buns_rem = (no_hotdogs * person) % 8

if hotdogs_rem == 0:
    min_hotdog_pack = (no_hotdogs * person) / 10
else:
    min_hotdog_pack = int(((no_hotdogs * person) / 10)) + 1
if buns_rem == 0:
    min_hotdog_buns_pack = (no_hotdogs * person) / 8
else:
    min_hotdog_buns_pack = int(((no_hotdogs * person) / 8)) + 1

leftover_hotdogs = (min_hotdog_pack * 10) - (no_hotdogs * person)
leftover_hotdog_buns = (min_hotdog_buns_pack * 8) - (no_hotdogs * person)

print(f"\nThe minimum number of packages of hot dogs required is {min_hotdog_pack}.")
print(
    f"The minimum number of packages of hot dog buns required is {min_hotdog_buns_pack}."
)
print(f"The number of hot dogs that will be left over is {leftover_hotdogs}.")
print(f"The number of hot dog buns that will be left over is {leftover_hotdog_buns}.")
