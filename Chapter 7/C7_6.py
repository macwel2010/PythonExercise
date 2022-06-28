import random


def roll(a):

    throws_list = []
    for i in range(1, a + 1):
        throws_list.append(random.randint(1, 6))
    return throws_list


number_of_throws = int(input("Enter the number of throws you want : "))
throws_list = roll(number_of_throws)
print(throws_list)
