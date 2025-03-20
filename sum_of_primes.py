#Given an input integer M. Write a Python program to find the sum of all prime numbers between 1 and M.
#Input : M = 10
#Output : 17 (2+3+5+7)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check up to sqrt(n)
        if n % i == 0:
            return False
    return True

def sum_of_primes(M):
    return sum(num for num in range(2, M + 1) if is_prime(num))

# Input
M = int(input())
print(sum_of_primes(M))
