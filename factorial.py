'''Factorial without Multiplication & Division
You are given a positive integer N. Your task is to compute the factorial of 
N without using any multiplication 
(∗) or division (/) operators.'''

def factorial(n):
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