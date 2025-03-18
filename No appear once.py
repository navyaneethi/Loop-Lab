'''You are given an array containing N integers where only one element is unique (appears exactly once), while all other elementsappear twice. Find and return the unique element. '''
'''arr = 5,3,2,3,2'''
'''output = 5'''

def unique_no(arr):
    return (sum(set(arr)))*2 - sum(arr)

arr = list(map(int,input().split(',')))
print(unique_no(arr))


or

def unique_no(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = list(map(int,input().split(',')))
print(unique_no(arr))
