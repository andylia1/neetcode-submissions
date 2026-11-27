# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, curr):
        if curr == None:
            return 0
        
        count = 1 + self.helper(curr.left)
        count2 = 1 + self.helper(curr.right)
        return max(count, count2)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)