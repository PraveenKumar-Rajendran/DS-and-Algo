class Solution:
    def countVowelStrings(self, n: int) -> int:
       
        # Recursive Approach
        def count_rec(n, not_be_less_than_this_char):
            if n==0:
                return 1
            total = 0
            for i in range(not_be_less_than_this_char,5):
                total += count_rec(n-1, i)
            return total
        
        return count_rec(n, 0)
    
# https://www.youtube.com/watch?v=tEWj6P-488M&t=1s