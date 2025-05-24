'''Check if a string is palindrome, ignoring the case.'''
s = input()
if s == s[::-1]:
    print("Palindrome.")
else:
    print("Not Palindrome.")