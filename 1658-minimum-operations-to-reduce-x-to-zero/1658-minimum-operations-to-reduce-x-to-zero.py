class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        # We need to make prefix_sum + suffix_sum = x. 
        # But instead of this, finding a subarray whose sum is sum(nums) - x will do the job.
        max_len, curr_sum, start_idx, found =0,0,0,False
        tot_len, target = len(nums) , sum(nums) - x
        
        for end_idx in range(tot_len):
            
            curr_sum += nums[end_idx]
            # If the sum of this sliding window (subarray) exceeds the target, 
            # keep reducing the window size (by increasing start_idx) until its sum becomes <= target
            while start_idx <= end_idx and curr_sum > target: 
                curr_sum -= nums[start_idx]
                start_idx += 1
            # If the sum becomes equal to the target, compare the length, and store if it exceeds the previous length.    
            if curr_sum == target:
                found = True
                max_len = max(max_len, end_idx - start_idx + 1)
        # Return -1 if the sum of the sliding window never becomes equal to target.    
        return tot_len - max_len if found else -1 

    
# Time Complexity: O(n)
# Space Complexity: O(1)
    
# Reference: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/2136555/C%2B%2BPython-Simple-Solution-w-Explanation-or-Sliding-Window


