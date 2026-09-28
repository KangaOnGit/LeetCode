# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def iterative_check(tree1, tree2):
            if tree1 is not None and tree2 is not None:
                if tree1.val != tree2.val:
                    return False
            else:
                return (tree1 == tree2)

            l = iterative_check(tree1.left, tree2.left)
            r = iterative_check(tree1.right, tree2.right)
            return (l and r)
        return iterative_check(p, q)