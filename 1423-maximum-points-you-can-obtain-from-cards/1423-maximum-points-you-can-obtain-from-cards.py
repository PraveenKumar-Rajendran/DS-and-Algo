class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        len_val = len(cardPoints)
        
        l, r = 0, len_val - k # sliding window of size (length-k)
        total = sum(cardPoints[r:]) # sum of leftover at the right
        res = total
        
        while r < len_val: # slide the window until we go out of bounds
            
            total += (cardPoints[l] - cardPoints[r]) # as we slide update the sum with only the leftover apart from the window
            res = max(res, total) # update result if new max value is found
            
            # update the window
            l+= 1
            r+= 1
        
        return res
        
# memory: O(1)
# Time: O(k+k)
        
# Reference: https://www.youtube.com/watch?v=TsA4vbtfCvo