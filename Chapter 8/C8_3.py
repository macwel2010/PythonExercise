date = input("Enter the date in the dd/mm/yyyy format : ")
month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
month = int(date[3:5])
print(month)
print(date[0:2], month_list[month - 1], date[6:10])
