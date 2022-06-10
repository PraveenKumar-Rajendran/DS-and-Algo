class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
#         # My old solution
#         len_required = []
#         required = []
#         for i in s:
#             if i not in required:
#                 required.append(i)
#                 print(required)
#             else:
#                 required.clear()
#                 required.append(i)
#             len_required.append(len(required))
            
#         return  max(len_required) if len(len_required) > 0 else 0
        
        # sliding window
        l = 0
        charSet = set()
        res = 0
        
        for r in range(len(s)): #right pointer
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1) # Store the max to result
        return res


# Reference: https://www.youtube.com/watch?v=wiGpQwVHdE0
    
    
        
        