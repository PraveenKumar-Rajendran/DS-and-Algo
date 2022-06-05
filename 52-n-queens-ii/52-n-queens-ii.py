class Solution:
    def totalNQueens(self, n: int) -> int:
        
        # note that we are not trying in a same row, so dont need to maintain a separate set.
        col = set() # To check if we are placing in a same column
        PosDiag = set() # r+c # To check if we are placing in a positive diagonal
        NegDiag = set() # r-c # To check if we are placing in a negative diagonal
        
        res = 0
        
        def backtrack(r):
            
            if r == n:
                nonlocal res # makes use of a variable that is declared before the function
                res += 1 # for each unique possible combination
                return
            
            for c in range(n):
                if c in col or (r+c) in PosDiag or (r-c) in NegDiag: # if there is a possiblity of attack skip it
                    continue
                
                # add unique values
                col.add(c)
                PosDiag.add(r+c)
                NegDiag.add(r-c)
                
                # continue back tracking
                backtrack(r+1)
                
                col.remove(c)
                PosDiag.remove(r+c)
                NegDiag.remove(r-c)
                
        backtrack(0)
        return res