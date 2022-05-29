class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        
        word_int = n*[0]
        word_len = n*[0]
        
        for i in range(n):
            mask,pos = 0,0
            for char in words[i]:
                pos = ord(char) - ord('a')
                mask |= 1 << pos #Bitwise set for the available characters at a single string
            word_int[i] = mask
            word_len[i] = len(words[i])
            
        max_prod = 0
        
        for i in range(n-1):
            for j in range(i+1,n):
                if (word_int[i] & word_int[j] == 0): # filter the words if they have a same character
                    max_prod = max(max_prod,word_len[i]*word_len[j])
        return max_prod
        
        
                        
        