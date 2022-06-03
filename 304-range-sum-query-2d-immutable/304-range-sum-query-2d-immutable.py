class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.SumMat = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.SumMat[r][c+1]
                self.SumMat[r+1][c+1] = prefix + above
                
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        
        bottomRight = self.SumMat[row2][col2]
        bottomLeft = self.SumMat[row2][col1 - 1]
        TopRight = self.SumMat[row1-1][col2]
        above = self.SumMat[row1-1][col1-1]
        
        return (bottomRight - bottomLeft - TopRight + above)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# Visual Explanation Reference: https://www.youtube.com/watch?v=KE8MQuwE2yA