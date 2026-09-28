# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check_LR(left, right):
            if left is not None and right is not None:
                if left.val != right.val:
                    return False
            else:
                return left == right
            l = check_LR(left.left, right.right)
            r = check_LR(left.right, right.left)
 
            return l and r
        return check_LR(root.left, root.right)