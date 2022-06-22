def calories():
    fat = float(input("Enter the grams of fat you have consumed : "))
    carb = float(input("Enter the grams of carbs you have consumed : "))
    cal_fat = fat * 9
    cal_carb = carb * 4
    print(f"The calories gained from fat is {cal_fat}.")
    print(f"The calories gained from carb is {cal_carb}.")


calories()
