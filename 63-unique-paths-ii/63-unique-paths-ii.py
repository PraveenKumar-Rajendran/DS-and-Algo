class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m_rows, n_cols = len(obstacleGrid), len(obstacleGrid[0])
        
        #Check the initial square
        if (obstacleGrid[0][0] == 1):
            return 0
         
        # if passed the above check set possible path 
        obstacleGrid[0][0] = 1
        
        # Filling the values for the first column # update possible paths
        for i in range(1,m_rows):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row # update possible paths        
        for j in range(1, n_cols):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        
        for i in range(1,m_rows): # Start searching from (1,1) square and sum from top and left squares
            for j in range(1,n_cols):
                
                if (obstacleGrid[i][j] == 0):
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
        return obstacleGrid[m_rows-1][n_cols-1] #Return possible unique paths to the destination
    
# Reference: Leetcode Solution

# Complexity Analysis

# Time Complexity: O(M×N). The rectangular grid given to us is of size M×N and we process each cell just once.
# Space Complexity: O(1). We are utilizing the obstacleGrid as the DP array. Hence, no extra space.