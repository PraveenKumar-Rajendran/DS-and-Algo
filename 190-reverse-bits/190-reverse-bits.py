class Solution:
    def reverseBits(self, n: int) -> int:
        
        s = str(bin(n))[2:][::-1] # Converting into binary and reversing it. # remember to ignore 'ob'
        
        while len(s) != 32: # append the remaining length of zeros at the right
            s += '0'
            
        return int(s, 2)  # convert binary string into decimal      
