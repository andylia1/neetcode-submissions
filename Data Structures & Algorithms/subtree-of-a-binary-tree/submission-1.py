# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(curr1, curr2):
            res = False
            res2 = False
            if not curr1:
                return res

            if curr1.val == curr2.val:
                res2 = isSame(curr1, curr2)
            
            
            return helper(curr1.right, curr2) or helper(curr1.left, curr2) or res2

        def isSame(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if (not curr1 or not curr2) or (curr1.val != curr2.val):
                return False

            return isSame(curr1.right, curr2.right) and isSame(curr1.left, curr2.left)

        return helper(root, subRoot)