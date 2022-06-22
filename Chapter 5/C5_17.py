number = int(input("Enter a number : "))


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


if is_prime(number):
    print("the number is a not prime number.")
else:
    print("the number is a prime number.")
