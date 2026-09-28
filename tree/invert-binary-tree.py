# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approaches:
            1. Swap Left and Right itself
            2. Swap Values (Doesn't work if there's None)
        Funny Cases:
            2 
           /
          3
        /
       1
        => 2
            \ 
             3
                \
                  1
        """
        if root is None:
            return root
        def invert(root):
            """
                Invert Left and Right Tree
            """
            if not root:
                return
            root.left, root.right = root.right, root.left
            # If it exists, swap
                # Don't stop even when 1 is None and the other isn't
            invert(root.left)
            invert(root.right)
        invert(root)
        return root