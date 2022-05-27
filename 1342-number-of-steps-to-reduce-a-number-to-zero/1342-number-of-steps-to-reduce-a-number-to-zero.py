class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        
        while num:
            num =  (num - 1) if (num%2) else (num >> 1)
            result += 1
        return result