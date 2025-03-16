n = int(input("Enter n: "))
diff = n  
num = 1
print(num)
''' We build each row as a list of strings that we then join and print. 
This improves readability and performance for larger inputs.'''
for i in range(1, n):
    row = []
    num += diff
    row.append(str(num))
    diff -= 1
    prev = num
    for j in range(i):
        prev = prev - diff - j
        row.append(str(prev))
    print(" ".join(row))
