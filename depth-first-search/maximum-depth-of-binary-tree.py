# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, count):
            if not root:
                return count
            count_left = dfs(root.left, count + 1)
            count_right = dfs(root.right, count + 1)

            return max(count_left, count_right)
        return dfs(root, 0)