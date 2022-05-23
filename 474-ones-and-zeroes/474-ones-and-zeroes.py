class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for s in strs:
            ones = s.count("1")
            zeros = len(s) - ones
            
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-zeros][j-ones])
            
        return dp[m][n]

        
# Reference: https://leetcode.com/problems/ones-and-zeroes/discuss/701736/Python-DP-Solution-explained-with-example