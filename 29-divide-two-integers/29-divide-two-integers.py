class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        #XOR
        sign = -1 if (dividend < 0) ^ (divisor < 0 ) else 1
        
        dividend = abs(dividend); divisor = abs(divisor)
        
        quotient = 0
        while(dividend >= divisor):
            tmp = divisor
            mul = 1
            while(dividend >= tmp):
                dividend -= tmp
                quotient += mul
                mul += mul
                tmp += tmp
            
        if sign == -1:
            quotient = - quotient
        
        #Bound check
        return min(2147483647,max(-2147483648,quotient))
        