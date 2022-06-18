class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # we get the base10 value by using 'int' method,
        # and add them together to get total value of base10
        # total value can be converted to binary string by 'bin' method
        
        # binary string returned by 'bin' leads with 'ob' thus we should ignore them.
        
        return bin(int(a,2)+int(b,2))[2:]