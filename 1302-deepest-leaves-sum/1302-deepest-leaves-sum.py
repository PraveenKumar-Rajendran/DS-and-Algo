# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
#         q = deque() # create queue
        
#         q.append((root, 0)) # push initial root and its depth
        
#         deep_sum = 0 # initialize output sum
#         max_depth = 0 # initialize maximum depth of a tree
        
#         while q: #loop until the end of the tree(BFS)
            
#             current, depth = q.popleft() # pop node and its depth
            
#             if depth>max_depth: # check if the depth is growing, then zero out the sum and reset new max depth
#                 deep_sum = 0
#                 max_depth = depth
                
#             if depth == max_depth: # sum the values in the max depth
#                 deep_sum += current.val
            
#             # if current node has left or right node append it, and increase the depth by 1
#             if current.left: q.append((current.left, depth+1)) 
#             if current.right: q.append((current.right, depth+1)) 
             
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)
    
# https://leetcode.com/problems/deepest-leaves-sum/discuss/463239/JavaC%2B%2BPython-Level-Traversal