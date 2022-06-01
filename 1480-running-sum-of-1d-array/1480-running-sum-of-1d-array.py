class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
#         length = len(nums)
#         dp = [0]*length
        
#         for i in range(length):
#             dp[i] += nums[i] + dp[i-1] 
            
            
#         return dp


        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            
        return nums