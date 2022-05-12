class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         def backtrack(comb, counter):
#             if len(comb) == len(nums):
#                 # make a deep copy of the resulting permutation,
#                 # since the permutation would be backtracked later.
#                 results.append(comb.copy())
#                 return

#             for num in counter:
#                 if counter[num] > 0:
#                     # add this number into the current combination
#                     comb.append(num) #push stack
#                     counter[num] -= 1
#                     # continue the exploration
#                     backtrack(comb, counter)
#                     # revert the choice for the next exploration
#                     comb.pop() #pop stack
#                     counter[num] += 1
        
#         counter = {n:0 for n in nums}
#         for n in nums:
#             counter[n] += 1
        
#         backtrack([], counter)

#         return results
        
        res = []
        perm = []
        
        counter = {n:0 for n in nums}
        for n in nums:
            counter[n] += 1   
            
        def backtrack():
            
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in counter: # loop through unique values
                if counter[n] > 0:
                    perm.append(n)
                    counter[n] -= 1
                    backtrack()
                    counter[n] += 1
                    perm.pop()
            
        backtrack()
        
        return res
            
            
            