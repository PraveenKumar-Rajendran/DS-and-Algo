class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [0] * (len(triangle)+ 1) # last row contains only zeros with one extra element to follow triangle structure
        #For each row we will need the minimum path sum in the row below
        
        #Bottom Up
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                                
                dp[i] = min(n+dp[i], n+dp[i+1]) # Store the minimum by checking minimum sum in the below row at adjacent positions
        
        return dp[0] #We need the value at first index since that will be minimum path sum of the root. #rest of the dp value might contain previous values.
        
        
        
        
# Reference: https://www.youtube.com/watch?v=OM1MTokvxs4
# Memory: O(n) n--> number of rows
# Time: O(n^2 approx 2n) --> Total number of elements in the array.