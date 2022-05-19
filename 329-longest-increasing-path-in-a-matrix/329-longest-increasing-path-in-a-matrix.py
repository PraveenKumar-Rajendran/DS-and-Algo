class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m_rows, n_cols = len(matrix), len(matrix[0])
        
        dp = {} #(r,c)
        
        def dfs(r,c, prevVal):
            
            if (r < 0 or r==m_rows or # check for out of bounds
                c < 0 or c==n_cols or # check for out of bounds
                matrix[r][c] <= prevVal): # check if the incoming value is equal equal or smaller
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)] #if the computed LIP is available return it
            
            res = 1
            
            res = max(res, 1+dfs(r+1, c, matrix[r][c])) #search for max result in all four directions, to get the max LIP
            res = max(res, 1+dfs(r-1, c, matrix[r][c]))
            res = max(res, 1+dfs(r, c+1, matrix[r][c]))
            res = max(res, 1+dfs(r, c-1, matrix[r][c]))
            
            dp[(r,c)] = res # add new LIP to dict
            
            return res
            
        for i in range(m_rows):
            for j in range(n_cols):
                dfs(i,j,-1) # search for LIPs in each values in the matrix of size mXn
                
        return max(dp.values()) # return the max LIP of the values in dp
 
'''

Reference
https://www.youtube.com/watch?v=wCc_nd-GiEc

'''

