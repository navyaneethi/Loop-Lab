'''Count Pairs divisible by 2
You're given a list of numbers. Your task is to find how many pairs of numbers in that list add 
up to an even number. A pair consists of two different numbers from the list. For example, in the 
list [1, 2, 3, 4], the pairs that sum to an even number are (1, 3) and (2, 4).

Input Format
    The first line of input will contain a single integer T
    T, denoting the number of test cases.
    Each test case consists of two lines of input.
    The first line of each test case contain N
    N, length of array arr, 
    The second line consist of the array arr.
Output Format
    For each test case, output on a new line the number of divisible pairs.

input 
3
4
6 1 2 3
6
2 2 1 7 5 3
2
4 8

output
2
7
1
'''

def count_even_sum_pairs(arr):
    even_count = sum(1 for num in arr if num%2==0)
    odd_count = len(arr)-even_count

    even_pair = (even_count*(even_count-1))//2
    odd_pair = (odd_count*(odd_count-1))//2
    return even_pair + odd_pair


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_even_sum_pairs(arr))
