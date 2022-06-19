class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        res = []
        products.sort() # sort the products to make sure matching words occur continuously
        
        l, r = 0, len(products)-1 # left at the top, right at the bottom
        
        for i in range(len(searchWord)):
            
            c = searchWord[i]
            
            # left, right pointer handle
            # skip words if it does not have enough chars or a mismatching char
            while l <= r and (len(products[l]) <= i or products[l][i] != c): 
                l += 1
            
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1            
            
            res.append([]) # creating list of lists as we loop through
            
            remain = r - l + 1 # total length of matching words
            
            for j in range(min(3, remain)): # loop through minimum 3 words or within bound
                
                res[-1].append(products[l+j]) # append matching words starting from the left pointer.
            
        return res
    
# Reference: https://www.youtube.com/watch?v=D4T2N0yAr20&t=2sf
# Time complexity is O(nlogn + n + m) where n is size of products, and m is length of searchWord.