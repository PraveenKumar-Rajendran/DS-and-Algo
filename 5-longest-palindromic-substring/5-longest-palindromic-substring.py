class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        # consider an odd palindrome case
        def pal_check(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                nonlocal resLen, res
                if (r-l+1) >  resLen:
                    
                    resLen = r-l+1
                    res = s[l:r+1]
                
                # shift points outwards at both end
                l -= 1 
                r += 1
        
        for i in range(len(s)):
            # For odd palindrome case
            # treating each char as a center of palindrome and using left and right pointers
            l, r = i, i
            pal_check(l,r)
            
            # For even palindrome case
            l,r = i, i+1
            pal_check(l,r)
            
        return res
                
# Time Complexity O(n^2)
# Memory Complexity O(1) maybe..
# Reference: https://www.youtube.com/watch?v=XYQecbcd6_c