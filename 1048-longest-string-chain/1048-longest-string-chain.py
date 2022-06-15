class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    dp[word] = dp[prev] + 1
                    res = max(res, dp[word])

        return res
    
# Reference: https://leetcode.com/problems/longest-string-chain/discuss/2153007/C%2B%2BPython-Simple-Solution-w-Explanation-or-DP