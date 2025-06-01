'''Find the length of the longest substring without repeating characters'''

def LongestUniqueSubstr (s):
    if len(s)==1 or len(s)==0:
        return len(s)
    
    left = 0
    right = 0
    res = 0
    vis = [False]*26

    while right < len(s):
        if vis[ord(s[right]) - ord('a')] == True:
            vis[ord(s[left]) - ord('a')] = False
            left+=1
        else:
            vis[ord(s[right]) - ord('a')] = True
            res = max(res, (right-left+1))
            right+=1
    return res
s = "abcbadbd"
#s ="a"
print(LongestUniqueSubstr(s))