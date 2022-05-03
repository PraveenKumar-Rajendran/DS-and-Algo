class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sorted_list = sorted(nums)
        start,end = len(nums),0
        
        for i in range(0,len(nums)):
            if nums[i] != sorted_list[i]:
                start = min(start, i)
                end = max(end, i)
        
        return (end-start+1) if (end - start) >= 0 else 0