def reverse_string(s):
    s1=''
    for c in s:
        s1=c+s1
    return s1
s=input()
print(reverse_string(s))