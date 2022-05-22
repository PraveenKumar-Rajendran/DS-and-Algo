class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            res += self.Count_Sub_Pal(s, i, i)
            res += self.Count_Sub_Pal(s, i, i+1)      
        return res
    
    def Count_Sub_Pal(self, s, l, r):
        count = 0
        while l>= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
    
# Reference: https://www.youtube.com/watch?v=4RACzI5-du8