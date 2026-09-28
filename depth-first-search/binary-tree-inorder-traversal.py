# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        inorder traversal -> Travel Left then Right
        """
        res = []
        def traverse(node, res):
            if node:
                # Travel Left
                traverse(node.left, res)

                # Save Node
                res.append(node.val)

                # Travel Right
                traverse(node.right, res)
            else:
                return

        traverse(root, res)
        return res