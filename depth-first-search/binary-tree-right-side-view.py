# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Intuition:
            Right Side View
                -> If you look at it level-by-level
                -> It will always take the right-most node
                -> BFS Appending from Left to Right
                    And take the value of the last node appended
                            (Right Node)
        """
        if not root: return []
        def bfs():
            res = []
            queue = [root]
            while queue:
                res.append(queue[-1].val)
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return res
        return bfs()