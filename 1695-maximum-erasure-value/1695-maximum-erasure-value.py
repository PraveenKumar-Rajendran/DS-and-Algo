class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Sliding window
        start_idx, currSum, maxSum = 0,0,0 
        unique_set = set()
        
        for end_idx in range(len(nums)):
            
            # if we find same element in the set remove elements until we remove the target element
            while nums[end_idx] in unique_set:
                unique_set.remove(nums[start_idx])
                currSum -= nums[start_idx]
                start_idx += 1
                
            # add it in the set otherwise    
            unique_set.add(nums[end_idx])
            currSum += nums[end_idx] # update the running sum
            end_idx += 1
            
            maxSum = max(maxSum, currSum) # Keep track of max of everything
            
        return maxSum
    
    
# Reference: https://leetcode.com/problems/maximum-erasure-value/discuss/1645653/WEEB-DOES-PYTHON-SLIDING-WINDOW-(BEATS-98.41)