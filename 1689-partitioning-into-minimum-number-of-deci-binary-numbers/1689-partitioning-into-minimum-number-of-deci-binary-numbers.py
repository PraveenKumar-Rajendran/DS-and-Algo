class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n)) # we need as many deci binary number as the max number in the given string