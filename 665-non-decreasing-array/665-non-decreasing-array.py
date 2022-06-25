class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        chance_used = False
        
        for i in range(len(nums)-1): # not to full lenght since we compare adjacent pairs
            if nums[i+1] >= nums[i]:
                continue
                
            if chance_used:
                return False
            
            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1] # firstly change the value[ind] with right val, only if right val is greater than the left val of val[ind]
            else:
                nums[i+1] = nums[i]  # if not change the rightval to be val[ind]
            
            chance_used = True
            
        return True
        
# Memory O(1)
# Time O(n)
# Reference: https://www.youtube.com/watch?v=RegQckCegDk&t=1s