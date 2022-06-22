def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        rem = number % i
        if rem == 0:
            count += 1
    if count > 2:
        status = True
    else:
        status = False
    return status


print("Thses are the prime numbers between 1 and 100.")
for j in range(2, 101):
    if is_prime(j) == False:
        print(j, end="  ")
