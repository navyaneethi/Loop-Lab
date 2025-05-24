s="amma"
rev=""

for c in s:
    rev = c+rev

if s==rev:
    print("Palindrome.")
else:
    print("Not a palindrome.")