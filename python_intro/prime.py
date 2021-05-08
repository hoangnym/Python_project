### Build a function to check whether something is prime or not

def prime_checker(num):
    if num <= 1: return "Number must be larger than 1"

    for i in range(2, num, 1):
        if num % i == 0:
            return f"{num} is not a prime number"

    return f"{num} is a prime number"


print(prime_checker(1))
print(prime_checker(2))
print(prime_checker(3))
print(prime_checker(4))
print(prime_checker(5))
print(prime_checker(6))
print(prime_checker(7))
print(prime_checker(8))
print(prime_checker(9))
print(prime_checker(17))

