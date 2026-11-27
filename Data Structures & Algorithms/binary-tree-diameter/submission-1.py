# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0

    def helper(self, curr):
        if curr == None:
            return 0
        
        left = self.helper(curr.left)
        right = self.helper(curr.right)

        self.res = max(self.res, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res