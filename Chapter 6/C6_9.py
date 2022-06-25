try:
    numbers = open(r"F:\Practice programms\Chapter 6\average_exception_C6_9.txt", "r")

except IOError:
    print("Check the file path.")

num = numbers.readline().rstrip()
sum = int(0)
count = 0

try:
    while num != "":
        count += 1
        sum = sum + int(num)
        num = numbers.readline().rstrip()
    print(f"The sum of the numbers is {sum}.")
    print(f"Average of all the numbers is {sum/count}")
except ValueError:
    print("Values entered are not valid.")
