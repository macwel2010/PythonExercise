numbers = open(r"F:\Practice programms\Chapter 6\sum_C6_5.txt", "r")
num = numbers.readline().rstrip()
sum = int(0)
while num != "":
    sum = sum + int(num)
    num = numbers.readline().rstrip()
print(f"The sum of the numbers is {sum}.")
