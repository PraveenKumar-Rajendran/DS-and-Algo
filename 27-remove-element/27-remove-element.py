class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_index_and_count = 0 
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[new_index_and_count] = nums[i]
                new_index_and_count += 1
        
        return new_index_and_count