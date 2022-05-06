class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = [] #To keep char and count
        
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1 # add count if it is available in the stack
            else:
                stack.append([c,1]) # append it if it is a new character
            
            if stack[-1][1] == k:
                stack.pop() # pop it if it reaches the k duplicates
        res = str() # Initialize string
        for char, count in stack:
            res += (char * count)
        
        return res
        