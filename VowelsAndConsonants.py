s = "Python Programming."
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
v_num = sum(1 for c in s if c in vowels)
c_num = len(s)-v_num
print("No. of vowels:", v_num)
print("No. of consonant:",c_num)
