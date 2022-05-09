class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits: 
            return []
        
        DigChar = {"2":"abc",
                   "3":"def",
                   "4":"ghi",
                   "5":"jkl",
                   "6":"mno",
                   "7":"pqrs",
                   "8":"tuv",
                   "9":"wxyz"}
        
        res = []
        
        def backtrack(i,curString):
            if len(digits) == len(curString):
                res.append(curString)
                return
            
            for c in DigChar[digits[i]]:
                backtrack(i+1,curString+c)
        
        backtrack(0,"")        
        return res