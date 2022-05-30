class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
#         #XOR
#         sign = -1 if (dividend < 0) ^ (divisor < 0 ) else 1
        
#         dividend = abs(dividend); divisor = abs(divisor)
        
#         quotient = 0
#         while(dividend >= divisor):
#             tmp = divisor
#             mul = 1
#             while(dividend >= tmp):
#                 dividend -= tmp
#                 quotient += mul
#                 mul += mul
#                 tmp += tmp
            
#         if sign == -1:
#             quotient = - quotient
        
#         #Bound check
#         return min(2147483647,max(-2147483648,quotient))
#https://leetcode.com/problems/divide-two-integers/discuss/2089426/100-or-0MS-or-3-WAYS-or-EXPLAINED-or-MEME

        if (dividend == -2147483648 and divisor == -1): return 2147483647
        
        a, b, res = abs(dividend), abs(divisor), 0
        
        for x in range(32)[::-1]:
            
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
                
        return res if (dividend > 0) == (divisor > 0) else -res
        