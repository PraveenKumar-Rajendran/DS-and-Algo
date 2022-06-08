class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: 
            return 0
        
        return 1 if s==s[::-1] else 2        
        
        
        
# Reference: https://leetcode.com/problems/remove-palindromic-subsequences/discuss/2124269/PYTHON-oror-EXPLAINED-oror
# https://leetcode.com/problems/remove-palindromic-subsequences/discuss/2126538/Python-And-Cpp-%3A-Runtime%3A-0-ms-faster-than-100.00