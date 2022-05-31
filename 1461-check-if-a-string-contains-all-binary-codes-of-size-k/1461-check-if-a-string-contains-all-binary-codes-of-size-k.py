class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        CodeSet = set()
        
        for i in range(len(s)-k+1):
            CodeSet.add(s[i:i+k]) #add every unique substring of length k to CodeSet
        
        # return True if the possible combinations of length 'k' is available in the CodeSet
        return len(CodeSet) == 2**k
        