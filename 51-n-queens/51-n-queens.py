class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        PosDiag = set() #r+c ==> maintains the sum(bottom left to top right)
        NegDiag = set() #r-c ==> maintains the difference(top left to bottom right)
        
        res = []
        board = [["."]*n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board] # make a string out of the row
                res.append(copy) # add the unique possible copy to the set
            
            for c in range(n):
                if c in col or (r+c) in PosDiag or (r-c) in NegDiag: #Check if it comes in same column or Positive Diag or negative diag if yes skip it.
                    continue
                
                # If passes then continue to add them in a set
                col.add(c)
                PosDiag.add(r+c)
                NegDiag.add(r-c)
                board[r][c] = "Q"
                
                # If call the next row for placing next queen
                backtrack(r+1)
                
                # Refresh the board
                col.remove(c)
                PosDiag.remove(r+c)
                NegDiag.remove(r-c)
                board[r][c] = "."
        
        #call backtracking from the first row
        backtrack(0)
        return res
    
# Reference: https://www.youtube.com/watch?v=Ph95IHmRp5M
    