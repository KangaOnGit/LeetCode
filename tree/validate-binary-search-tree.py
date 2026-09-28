# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        EVERY NODE to the RIGHT/LEFT of the TREE must be GREATER/LESSER than the ROOT
            You can either do Breadth-First Search (My favourite) -> Queue
            Or you can do Depth-First Search -> Stack
        Depth First Search is easier since we can just check
                if every value from left/right to less/larger than root
        
        Or we can do Inorder Traversal since it's strictly increasing
            [Left Tree] -> Root -> [Right Tree]
        """
        prev = None
        def inOrder_traversal(root):
            nonlocal prev
            if not root:
                True

            # Check left side
            left = inOrder_traversal(root.left)
            if not left:
                return False

            # Since inorder traversal is STRICTLY INCREASING
                # If current value is equal or smaller than previous value
                    # -> It's not obeying Strictlying Increasing -> False
            if prev is not None and root.val <= prev:
                return False
            
            prev = root.val

            # Check right side
            right = inOrder_traversal(root.right)

            return right
        #return inOrder_traversal(root)
        def dfs(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
                
            return (
                dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high)
            )
        return dfs(root, float('-inf'), float('inf'))


