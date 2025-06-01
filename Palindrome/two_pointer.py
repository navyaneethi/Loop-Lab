s = "raceCar"
s=s.lower()
i=0
j=len(s)-1
while(i<j):
    if s[i]==s[j]:
        i+=1
        j-=1
    else:
        print("Not a palindrome.")
        break
if i>=j:
    print("Is a palindrome.")        