class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # dp[i][j] refers to the number of deletions required to equalize the two strings 
        
        # if we consider the strings' length upto (i-1)th index and (j-1)th index for s1 and s2 respectively
        for i in range(1,len(word2)+1):
            dp[0][i]=i
        for j in range(1,len(word1)+1):
            dp[j][0]= j
        
        
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                    
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # no change since the same character put the diagonal in the same character
                    
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1 
                    # Increment 1 since we need to delete either one of the character and add it to the previous minimum
                    
                    
        return dp[-1][-1] # dp[m][n] gives the required minimum number of deletions
    
# Reference: https://leetcode.com/problems/delete-operation-for-two-strings/solution/

# Complexity Analysis

# Time complexity : O(m*n). We need to fill in the dpdp array of size mmxnn. Here, m and n refer to the lengths of s1 and s2.

# Space complexity : O(m*n). dp array of size mxn is used.
    
