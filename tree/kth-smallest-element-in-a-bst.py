# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Inorder Traversal?
            Inorder Travel of a BST always go from Left-Most -> Root -> Right
            -> It goes from Lowest -> Highest
        """
        
        count = 0
        smallest_val = None
        def inorder_traversal(
            root: TreeNode,
            ):
            nonlocal count
            nonlocal smallest_val

            if root is None:
                return

            # go left
            inorder_traversal(root.left)
            
            count += 1
            if count <= k:
                smallest_val = root.val

            # go right
            inorder_traversal(root.right)
        inorder_traversal(root)
        return smallest_val