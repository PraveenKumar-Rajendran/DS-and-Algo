class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Sum approach
        # res = len(nums)
        # for i in range(len(nums)):
        #     res +=  (i- nums[i])
        # return res
        
        #XOR Approach
        res = len(nums)
        for i in range(len(nums)):
            res ^= (i^nums[i])
        return res
            