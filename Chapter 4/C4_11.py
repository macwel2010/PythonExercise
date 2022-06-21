print("Enter the hours of sleep you are taking on each day as prompted. ")
user_sleep_list = []
for i in range(1, 8):
    user_sleep = int(input(f"Enter the hours of sleep for day {i} : "))
    user_sleep_list.append(user_sleep)
total_user_sleep = sum(user_sleep_list)
desired_sleep = 7 * 8
sleep_dept = total_user_sleep - desired_sleep
if sleep_dept > 0:
    print("You sleep more than required.")
elif sleep_dept < 0:
    print("You sleep less than required.")
elif sleep_dept == 0:
    print("You sleep optimally.")
