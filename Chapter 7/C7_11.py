magic_square_list = []

for j in range(3):
    t = []
    for i in range(3):
        number = int(input(f"Enter {i+1},{j+1} number : "))
        t.append(number)
    magic_square_list.append(t)


def magic_square(square_list):
    print("\nThe square is :  ")
    for i in square_list:
        print(i)

    sum_list = []

    for i in range(len(square_list)):
        sum1 = square_list[i][0] + square_list[i][1] + square_list[i][2]
        sum2 = square_list[0][i] + square_list[1][i] + square_list[2][i]
        sum_list.append(sum1)
        sum_list.append(sum2)
    sum3 = square_list[0][0] + square_list[1][1] + square_list[2][2]
    sum4 = square_list[2][0] + square_list[1][1] + square_list[0][2]
    sum_list.append(sum3)
    sum_list.append(sum4)
    count = 0
    for i in sum_list:
        if i == sum_list[0]:
            count += 1

    if count == 8:
        print("\nThe square is magic square.")
    else:
        print("The square is not a magic square.")


magic_square(magic_square_list)
