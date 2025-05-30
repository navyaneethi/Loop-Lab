n = int(input())
diff = n
num = 1
print(num)
for i in range(1,n):
    num+=diff
    print(num,end=" ")
    diff-=1
    prev = num
    for j in range(i):
        prev=prev-diff-j
        print(prev,end=" ")
    print()
