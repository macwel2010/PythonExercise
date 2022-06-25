numbers = open(r"F:\Practice programms\Chapter 6\average_C6_6.txt", "r")
num = numbers.readline().rstrip()
sum = int(0)
count = 0
while num != "":
    count += 1
    sum = sum + int(num)
    num = numbers.readline().rstrip()
print(f"The sum of the numbers is {sum}.")
print(f"Average of all the numbers is {sum/count}")
