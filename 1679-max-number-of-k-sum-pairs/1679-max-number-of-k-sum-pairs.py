class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left, right = 0, len(nums)-1
        count = 0
        while(left<right):
            check_val = nums[left]+nums[right]
            if check_val == k:
                left +=1
                right -=1
                count += 1
            elif check_val > k:
                right -= 1
            else:
                left += 1
                
        return count