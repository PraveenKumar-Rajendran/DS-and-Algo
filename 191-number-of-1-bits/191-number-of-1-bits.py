class Solution:
    def hammingWeight(self, n: int) -> int:
        
        
        result = 0
        for i in range(32):
            result += ((n & (1 << i)) != 0)
        return result