class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index at nums1 (it has length to accomodate both list)
        last = m + n -1
        
        # place value in reverse order
        
        while n>0 and m>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
            
        while n > 0:
            nums1[last] = nums2[n-1]
            last, n = last-1, n-1
        
# Refernce: https://www.youtube.com/watch?v=P1Ic85RarKY