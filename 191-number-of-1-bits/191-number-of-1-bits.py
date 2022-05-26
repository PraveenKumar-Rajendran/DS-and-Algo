class Solution:
    def hammingWeight(self, n: int) -> int:
        
        
        Hamming_weight = 0
        
        while n:
            n = n & (n-1) # Eleminates a set bit each time thus making it zero after the set bits are over
            Hamming_weight += 1
            
        return Hamming_weight
        