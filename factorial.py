'''Factorial without Multiplication & Division
You are given a positive integer N. Your task is to compute the factorial of 
N without using any multiplication 
(∗) or division (/) operators.'''

def factorial(n):
    if n == 1 or n == 0:
        return 1  # Fixing base case
    if n == 2:
        return 2  # Fixing case for n=2
    
    temp=n
    for i in range(n,2,-1):
        fact=0 
        for _ in range(i-1):
            fact+=temp
        temp = fact
    return fact
t = int(input())
for _ in range(t):
    n = int(input())
    print(factorial(n))
