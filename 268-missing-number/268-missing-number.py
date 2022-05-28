class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # # Sum approach
        # res = len(nums)
        # for i in range(len(nums)):
        #     res +=  (i- nums[i])
        # return res
        
        #XOR Approach
        res = len(nums)
        for i in range(len(nums)):
            res ^= (i^nums[i])
        return res
        
        # #Gauss
        # return int((len(nums)*(len(nums) + 1) / 2) - sum(nums))
            