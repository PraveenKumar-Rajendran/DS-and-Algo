class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        left, right, maxlen = 0,0,0
        
        #forward pass
        for i in s:
            if i is '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                maxlen = max(maxlen,2*left)
            if right > left:
                left, right = 0, 0
        
        left, right = 0, 0
        #backward pass    
        for i in s[::-1]:
            if i is ')':
                right += 1
            else:
                left += 1
                
            if left == right:
                maxlen = max(maxlen,2*left)
            if left > right:
                left, right = 0, 0
        
        return maxlen
    
    # reference: Leetcode Java Solution
    # Complexity Analysis

    # Time complexity: O(n). Two traversals of the string.

    # Space complexity: O(1). Only two extra variables left and right are needed.