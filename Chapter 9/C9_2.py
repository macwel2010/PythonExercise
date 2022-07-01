import random

capital_dict = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun ",
    "West Bengal": "Kolkata",
}
right = 0
wrong = 0

while True:
    again = input("press q to Quit and enter to continue.")
    if again == "q":
        print(f"You gave {right} right answers and {wrong} wrong answers. ")
        break
    else:
        i = random.randint(1, 28)
        cap_ans = input(f"What is the capital of {list(capital_dict.keys())[i]}? ")
        if cap_ans == capital_dict[list(capital_dict.keys())[i]]:
            print("yes! you are right!!!!")
            right += 1
        else:
            print("No! you are wrong!!!!")
            wrong += 1
