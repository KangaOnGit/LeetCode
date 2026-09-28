# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Intuition:
            Looks exactly like a DFS
                How to make it into a DFS?
            Notice: A Node is good IF
                        It is larger than the LARGEST Node SEEN SO FAR
                    => Update Largest Node as we travel
                    => max(largest_node.val, root.val)
        """
        if not root:
            return 0
        count = 0
        def dfs(root, high):
            nonlocal count
            if not root:
                return
            if root.val >= high:
                count += 1
            dfs(root.left, high = max(root.val, high))
            dfs(root.right, high = max(root.val, high))
        dfs(root, root.val)
        return count