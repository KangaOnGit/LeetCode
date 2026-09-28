# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """ 
        Intuition:
            Similar to the "is Same Tree?" problem
            move left and right til root = subroot
                then we check from that root if it's the same tree
        """
        res = False
        def check_subTree(root, subRoot):
            nonlocal res

            # if root is not None and have same value
            if root and root.val == subRoot.val:
                # check if same tree
                res = (res or self.isSameTree(root, subRoot))
            # even if found the starting node
                # don't stop finding more roots 
                # i.e: root [1, 1] | subroot [1]
            if root:
                check_subTree(root.left, subRoot)
                check_subTree(root.right, subRoot)
        check_subTree(root, subRoot)
        return res

    def isSameTree(self, root, subRoot):
        # if both is None
        if not root and not subRoot:
            return True
        # if one is None
        elif (root and not subRoot) or (not root and subRoot):
            return False
        # both not None but diff value
        elif root.val != subRoot.val:
            return False

        # Check if left and right is the same
        left = self.isSameTree(root.left, subRoot.left)
        right = self.isSameTree(root.right, subRoot.right)

        return (left and right)