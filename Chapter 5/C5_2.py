string = input("Enter the string : ")
number = int(input("Enter the times you want to repeat the string : "))


def repeat(string, number):
    for i in range(number):
        print(string)


repeat(string, number)
