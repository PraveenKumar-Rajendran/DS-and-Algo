class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        n = len(envelopes)
        
        if n <= 1:
            return n
        
        envelopes.sort(key=lambda x:(x[0],-x[1]))  # sort by width(ascending), then by height(descending) for a tie width values 
        h = []
        
        for envelop in envelopes:
            j = bisect.bisect_left(h,envelop[1]) # search for a possible position
            
            if j < len(h):
                
                h[j] = envelop[1] # if position is lesser than already available elements then replace at that index
            
            else:
                
                h.append(envelop[1]) # if not append at the end and increase the length of the list'
                
        return len(h)
                
        
        
        
# https://leetcode.com/problems/russian-doll-envelopes/discuss/82761/Python-O(nlogn)-O(n)-solution-beats-97-with-explanation  

# Time: O(nlogn)
# Space: O(n)
        
        