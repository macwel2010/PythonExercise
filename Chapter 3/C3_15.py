sec = int(input("Enter the number of seconds : "))

day = sec // (24 * 3600)
secd = sec % (24 * 3600)
hour = secd // (3600)
secd = secd % 3600
minute = secd // 60
secd = secd % 60

if sec < 60:
    print(f"{secd} seconds ")
elif sec < 3600:
    print(f"{minute} minutes : {secd} seconds")
elif sec < 86400:
    print(f"{hour} hours : {minute} minutes : {secd} seconds")
else:
    print(f"{day} days : {hour} hours : {minute} minutes : {secd} sesonds")
